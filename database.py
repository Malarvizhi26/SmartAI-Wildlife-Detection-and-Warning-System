import sqlite3
import datetime

DB_NAME = "wildlife_alerts.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS alerts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            animal_name TEXT NOT NULL,
            confidence REAL NOT NULL,
            timestamp TEXT NOT NULL,
            email_sent INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    conn.close()

def save_alert(animal_name, confidence, email_sent=0):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO alerts (animal_name, confidence, timestamp, email_sent) VALUES (?, ?, ?, ?)",
        (animal_name, confidence, timestamp, email_sent)
    )
    conn.commit()
    conn.close()

def get_all_alerts():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alerts ORDER BY id DESC")
    alerts = cursor.fetchall()
    conn.close()
    return alerts

def get_stats():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute("SELECT COUNT(*) FROM alerts")
    total = cursor.fetchone()[0]
    
    cursor.execute("SELECT animal_name, COUNT(*) as count FROM alerts GROUP BY animal_name ORDER BY count DESC")
    by_animal = cursor.fetchall()
    
    cursor.execute("SELECT COUNT(*) FROM alerts WHERE email_sent = 1")
    emails_sent = cursor.fetchone()[0]
    
    conn.close()
    return {"total": total, "by_animal": by_animal, "emails_sent": emails_sent}
