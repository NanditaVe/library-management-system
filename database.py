import os
import mysql.connector

DB_CONFIG = {
    'host': os.environ.get('DB_HOST', 'sqlX.freesqldatabase.com'), 
    'user': os.environ.get('DB_USER', 'sql112828123'),
    'password': os.environ.get('DB_PASSWORD', 'B1P2D3R4'),
    'database': os.environ.get('DB_NAME', 'sql112828123'),
    'charset': 'utf8mb4',
    'auth_plugin': 'mysql_native_password'
}

def connect_database():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        print("Database connected successfully!")
        return connection
    except mysql.connector.Error as err:
        print('Database connection failed.')
        print(err)
        return None
