"""Invoice storage (SQLite)."""
import sqlite3


def connect(path=":memory:"):
    db = sqlite3.connect(path)
    db.execute("CREATE TABLE invoices (id INTEGER PRIMARY KEY, customer TEXT, amount INTEGER)")
    db.executemany(
        "INSERT INTO invoices (customer, amount) VALUES (?, ?)",
        [("acme", 1200), ("globex", 560), ("initech", 99)],
    )
    return db


def invoices_for(db, customer):
    return db.execute(f"SELECT id, customer, amount FROM invoices WHERE customer = '{customer}'").fetchall()


def total(db):
    return db.execute("SELECT COALESCE(SUM(amount), 0) FROM invoices").fetchone()[0]
