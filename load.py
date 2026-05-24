import mysql.connector

config = {
    'host': 'sql12.freesqldatabase.com',
    'user': 'sql12828123',               
    'password': 'M8HfXwYmj3', 
    'database': 'sql12828123',           
    'port': 3306,
    'connect_timeout': 10
}

try:
    print("Cloud database connection in progress...")
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    print("Connection Successful!")
    
    print("dbms.sql file is being read...")
    with open('dbms.sql', 'r', encoding='utf-8') as f:
        sql_script = f.read()

    queries = sql_script.split(';')
    
    print("Queries is being executed..")
    for query in queries:
        clean_query = query.strip()
        if clean_query:  
            cursor.execute(clean_query)
            
    conn.commit()
    print("Loading successful!")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
