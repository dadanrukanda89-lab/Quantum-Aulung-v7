import sqlite3
import os

def inisialisasi_db():
    if not os.path.exists('data'):
        os.makedirs('data')
    conn = sqlite3.connect('data/quantum.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS master 
                      (id INTEGER PRIMARY KEY, nama TEXT)''')
    conn.commit()
    conn.close()

def simpan_master(nama):
    conn = sqlite3.connect('data/quantum.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM master")
    cursor.execute("INSERT INTO master (nama) VALUES (?)", (nama,))
    conn.commit()
    conn.close()

def ambil_master():
    conn = sqlite3.connect('data/quantum.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nama FROM master")
    data = cursor.fetchone()
    conn.close()
    return data[0] if data else "Stranger"

