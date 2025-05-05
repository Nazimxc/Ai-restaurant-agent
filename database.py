import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def connect():
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DATABASE", "restaurant")
    )

def create_table():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservations (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255),
            contact VARCHAR(50),
            time_slot VARCHAR(50),
            guests INT
        )
    """)
    conn.commit()
    conn.close()

def add_reservation(name, contact, time_slot, guests):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reservations (name, contact, time_slot, guests) VALUES (%s, %s, %s, %s)", (name, contact, time_slot, guests))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print("❌ MySQL Error:", e)
        return False

def get_all_reservations():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, contact, time_slot, guests FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows
