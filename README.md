# Library Management System

A school library management system with two interfaces:
- **Web app** (Flask + MySQL) — browser-based dashboard
- **CLI app** (Python + MySQL) — terminal-based menu system

## Project Structure

```
library_management/
├── app.py               # Flask web application
├── main.py              # CLI entry point
├── database.py          # DB connection config
├── books.py             # CLI: book operations
├── students.py          # CLI: student operations
├── teachers.py          # CLI: teacher operations
├── issue_return.py      # CLI: issue & return logic
├── utils.py             # Shared utilities (print_table)
├── dbms.sql             # MySQL database dump
└── templates/
    ├── base.html        # Shared layout with sidebar
    ├── home.html        # Dashboard
    ├── books.html       # Book catalogue (read-only)
    ├── students.html    # Student records (CRUD)
    └── teachers.html    # Teacher records (CRUD)
```

## Setup

### 1. Database
```sql
mysql -u root -p < dbms.sql
```
This creates the `library_management_system` database with all tables and sample data.

### 2. Install dependencies
```bash
pip install flask mysql-connector-python tabulate
```

### 3. Configure DB password

**Web app** — edit `app.py`, line with `password=`:
```python
password="YOUR_MYSQL_PASSWORD",
```

**CLI app** — edit `database.py`:
```python
'password': 'YOUR_MYSQL_PASSWORD',
```

### 4. Run

**Web app:**
```bash
python app.py
```
Then open http://localhost:5000

**CLI app:**
```bash
python main.py
```

## Features

### Web App
| Page | Features |
|------|----------|
| Dashboard | Stats overview, pending issues, genre breakdown |
| Book Records | Search by title/author/genre, filter by genre tab, read-only |
| Student Records | Search, add new student, edit book/date/status |
| Teacher Records | Search, add new teacher, edit book/date/status |

### CLI App
| Menu | Features |
|------|----------|
| Book Records | View all, search, add, update, delete |
| Student Records | View all, add student |
| Teacher Records | View all, add teacher |
| Issue Book | Issue to student with due date |
| Return Book | Return with automatic fine calculation (₹5/day after 7 days) |

## Tech Stack
- **Backend:** Python 3, Flask
- **Database:** MySQL 8
- **Frontend:** Jinja2 templates, vanilla HTML/CSS/JS
- **CLI:** tabulate for formatted table output
