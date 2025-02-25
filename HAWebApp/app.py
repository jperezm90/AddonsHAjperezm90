from flask import Flask
import sqlite3

app = Flask(__name__)

# Initialize a simple SQLite database
def init_db():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY, value TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Welcome to HAWebApp!"

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5001)