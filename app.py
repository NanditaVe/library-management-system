import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'library_secret_key'

def get_db():
    return mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'sqlX.freesqldatabase.com'),
        user=os.environ.get('DB_USER', 'sql112828123'),
        password=os.environ.get('DB_PASSWORD', 'M8HfXwYmj3'),
        database=os.environ.get('DB_NAME', 'sql112828123'),
        charset='utf8mb4',
        auth_plugin='mysql_native_password'
    )

# ── Home / Dashboard ──────────────────────────────────────────────────────────
@app.route('/')
def home():
    conn = get_db()
    cur  = conn.cursor(dictionary=True)

    cur.execute("SELECT COUNT(*) AS cnt FROM books_records")
    total_books = cur.fetchone()['cnt']

    cur.execute("SELECT COUNT(*) AS cnt FROM student_records")
    total_students = cur.fetchone()['cnt']

    cur.execute("SELECT COUNT(*) AS cnt FROM teacher_records")
    total_teachers = cur.fetchone()['cnt']

    cur.execute("SELECT COUNT(*) AS cnt FROM student_records WHERE Return_Status = 'Pending'")
    student_pending = cur.fetchone()['cnt']

    cur.execute("SELECT COUNT(*) AS cnt FROM teacher_records WHERE Return_Status = 'Pending'")
    teacher_pending = cur.fetchone()['cnt']
    total_pending = student_pending + teacher_pending

    cur.execute("""
        SELECT Student_Name AS name, Book_Issued AS book, Issue_Date AS date, 'Student' AS role
        FROM student_records WHERE Return_Status = 'Pending'
        UNION ALL
        SELECT Teacher_Name, Book_Issued, Issue_Date, 'Teacher'
        FROM teacher_records WHERE Return_Status = 'Pending'
        ORDER BY date
    """)
    pending_list = cur.fetchall()

    cur.execute("SELECT Genre, COUNT(*) AS cnt FROM books_records GROUP BY Genre ORDER BY cnt DESC")
    genres = cur.fetchall()

    cur.close(); conn.close()
    return render_template('home.html',
        total_books=total_books,
        total_students=total_students,
        total_teachers=total_teachers,
        total_pending=total_pending,
        pending_list=pending_list,
        genres=genres
    )

# ── Books ─────────────────────────────────────────────────────────────────────
@app.route('/books')
def view_books():
    conn = get_db()
    cur  = conn.cursor(dictionary=True)
    q    = request.args.get('q', '')
    genre = request.args.get('genre', '')
    sql  = "SELECT * FROM books_records WHERE 1=1"
    params = []
    if q:
        sql += " AND (Name LIKE %s OR Author LIKE %s OR Genre LIKE %s)"
        params += [f'%{q}%', f'%{q}%', f'%{q}%']
    if genre:
        sql += " AND Genre = %s"
        params.append(genre)
    sql += " ORDER BY Name"
    cur.execute(sql, params)
    books = cur.fetchall()
    cur.execute("SELECT DISTINCT Genre FROM books_records ORDER BY Genre")
    genres = [r['Genre'] for r in cur.fetchall()]
    cur.close(); conn.close()
    return render_template('books.html', books=books, genres=genres, q=q, active_genre=genre)

# ── Students ──────────────────────────────────────────────────────────────────
@app.route('/students')
def view_students():
    conn = get_db()
    cur  = conn.cursor(dictionary=True)
    q    = request.args.get('q', '')
    sql  = "SELECT * FROM student_records WHERE 1=1"
    params = []
    if q:
        sql += " AND (Student_Name LIKE %s OR Book_Issued LIKE %s OR Class LIKE %s)"
        params += [f'%{q}%', f'%{q}%', f'%{q}%']
    sql += " ORDER BY Class, Section, Roll_No"
    cur.execute(sql, params)
    students = cur.fetchall()
    cur.close(); conn.close()
    return render_template('students.html', students=students, q=q)

@app.route('/students/add', methods=['POST'])
def add_student():
    name = request.form['name'].strip()
    cls  = request.form['cls'].strip()
    sec  = request.form['section'].strip()
    roll = request.form['roll'].strip()
    conn = get_db(); cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO student_records (Student_Name, Class, Section, Roll_No) VALUES (%s,%s,%s,%s)",
            (name, cls, sec, roll)
        )
        conn.commit()
        flash('Student added successfully.', 'success')
    except Exception as e:
        conn.rollback()
        flash(f'Error: {e}', 'danger')
    finally:
        cur.close(); conn.close()
    return redirect(url_for('view_students'))

@app.route('/students/update/<int:admno>', methods=['POST'])
def update_student(admno):
    book   = request.form.get('book', '').strip() or None
    date   = request.form.get('date', '').strip() or None
    status = request.form.get('status', '').strip() or None
    conn = get_db(); cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE student_records
            SET Book_Issued=%s, Issue_Date=%s, Return_Status=%s
            WHERE Admno=%s
        """, (book, date, status, admno))
        conn.commit()
        flash('Student record updated.', 'success')
    except Exception as e:
        conn.rollback()
        flash(f'Error: {e}', 'danger')
    finally:
        cur.close(); conn.close()
    return redirect(url_for('view_students'))

# ── Teachers ──────────────────────────────────────────────────────────────────
@app.route('/teachers')
def view_teachers():
    conn = get_db()
    cur  = conn.cursor(dictionary=True)
    q    = request.args.get('q', '')
    sql  = "SELECT * FROM teacher_records WHERE 1=1"
    params = []
    if q:
        sql += " AND (Teacher_Name LIKE %s OR Book_Issued LIKE %s)"
        params += [f'%{q}%', f'%{q}%']
    sql += " ORDER BY Teacher_Name"
    cur.execute(sql, params)
    teachers = cur.fetchall()
    cur.close(); conn.close()
    return render_template('teachers.html', teachers=teachers, q=q)

@app.route('/teachers/add', methods=['POST'])
def add_teacher():
    name = request.form['name'].strip()
    conn = get_db(); cur = conn.cursor()
    try:
        cur.execute("INSERT INTO teacher_records (Teacher_Name) VALUES (%s)", (name,))
        conn.commit()
        flash('Teacher added successfully.', 'success')
    except Exception as e:
        conn.rollback()
        flash(f'Error: {e}', 'danger')
    finally:
        cur.close(); conn.close()
    return redirect(url_for('view_teachers'))

@app.route('/teachers/update/<int:id_no>', methods=['POST'])
def update_teacher(id_no):
    book   = request.form.get('book', '').strip() or None
    date   = request.form.get('date', '').strip() or None
    status = request.form.get('status', '').strip() or None
    conn = get_db(); cur = conn.cursor()
    try:
        cur.execute("""
            UPDATE teacher_records
            SET Book_Issued=%s, Issue_Date=%s, Return_Status=%s
            WHERE Id_No=%s
        """, (book, date, status, id_no))
        conn.commit()
        flash('Teacher record updated.', 'success')
    except Exception as e:
        conn.rollback()
        flash(f'Error: {e}', 'danger')
    finally:
        cur.close(); conn.close()
    return redirect(url_for('view_teachers'))

if __name__ == '__main__':
    app.run(debug=True)
