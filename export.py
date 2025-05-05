# export.py
import pandas as pd
from database import connect

def export_to_excel(filename="reservations.xlsx"):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(rows, columns=columns)
    df.to_excel(filename, index=False)
    print(f"📁 Reservations exported to {filename}")
    cursor.close()
    conn.close()
