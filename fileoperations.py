import sqlite3

DB_NAME = 'budget.db'

DEFAULT_CATEGORIES = ["hrana", "najemnina", "transport", "zabava", "zdravje", "ostalo"]

def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def initialize_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL UNIQUE
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id          INTEGER PRIMARY KEY AUTOINCREMENT,
            amount      REAL NOT NULL,
            description TEXT,
            date        TEXT NOT NULL,
            category_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES categories(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            key   TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

def load_categories():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM categories ORDER BY name")
    rows = cursor.fetchall()

    conn.close()

    if not rows:
        for cat in DEFAULT_CATEGORIES:
            save_category(cat)
        return DEFAULT_CATEGORIES.copy()

    return [row[0] for row in rows]

def save_category(name):
    conn = get_connection()              # 1. get connection
    cursor = conn.cursor()               # 2. get cursor
    cursor.execute(                      # 3. execute SQL
        "INSERT OR IGNORE INTO categories (name) VALUES (?)", 
        (name,)                          # this is what replaces the ?
    )
    conn.commit()                        # 4. commit
    conn.close()                         # 5. close

def delete_category(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM categories WHERE name = ?",
        (name,)
    )
    conn.commit()
    conn.close()

def load_expenses():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT e.id, e.amount, e.description, e.date, c.name
        FROM expenses e
        JOIN categories c ON e.category_id = c.id
    ''')
    rows = cursor.fetchall()
    conn.close()
    return [
        {
            "id":          row[0],
            "amount":      row[1],
            "description": row[2],
            "date":        row[3],
            "category":    row[4]
        }
        for row in rows
    ]

def save_expense(amount, description, date, category_name):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT id FROM categories WHERE name = ?", (category_name,))
    row = cursor.fetchone()
    
    if row is None:
        print(f"Kategorija '{category_name}' ne obstaja!")
        conn.close()
        return
    
    category_id = row[0]
    cursor.execute(
        "INSERT INTO expenses (amount, description, date, category_id) VALUES (?, ?, ?, ?)",
        (amount, description, date, category_id)
    )
    conn.commit()
    conn.close()

def db_delete_expense(expense_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )
    conn.commit()
    conn.close()

def load_settings():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM settings")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return {"monthly_budget": 0.0}

    settings = {}
    for row in rows:
        settings[row[0]] = float(row[1])
    return settings

def save_settings(settings):
    conn = get_connection()
    cursor = conn.cursor()
    for key, value in settings.items():
        cursor.execute(
            "INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)",
            (key, value)
        )
    conn.commit()
    conn.close()

def reassign_category(old_name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE expenses 
SET category_id = (SELECT id FROM categories WHERE name = 'ostalo')
WHERE category_id = (SELECT id FROM categories WHERE name = ?)
       ''', (old_name,) )
    conn.commit()
    conn.close()