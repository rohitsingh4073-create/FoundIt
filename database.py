import sqlite3
from Models.item_report import LostReport, FoundReport

def init_db():

    conn = sqlite3.connect("foundit.db")

    cursor = conn.cursor()

    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        password_hash TEXT
        )
    """
    )

    conn.commit()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute(
        """ CREATE TABLE IF NOT EXISTS reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT, 
        description TEXT,
        category TEXT, 
        location TEXT,
        date TEXT,
        report_type TEXT CHECK(report_type IN ('lost' , 'found') ),
        FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """
    )

    conn.commit()

    conn.close()



def add_report(report, user_id):
    conn = sqlite3.connect('foundit.db')
    cursor = conn.cursor()

    if isinstance(report, LostReport):
        cursor.execute(
            "INSERT INTO reports (user_id, title, description, category, location, date, report_type) VALUES ( ?, ?, ?, ?, ?, ?, ?)",
            (user_id, report.title, report.description, report.category, report.location, report.last_seen_date, 'lost')
        )
        report_id = cursor.lastrowid
        conn.commit()
        conn.close()
        print("Reported successfully.")
        return report_id

    if isinstance(report, FoundReport):
        cursor.execute(
            "INSERT INTO reports (user_id, title, description, category, location, date, report_type) VALUES ( ?, ?, ?, ?, ?, ?, ?)",
            (user_id, report.title, report.description, report.category, report.location, report.found_date, 'found')
        )
        report_id = cursor.lastrowid
        conn.commit()
        conn.close()
        print("Reported Successfully")
        return report_id




def get_all_reports():
    conn = sqlite3.connect('foundit.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reports")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    conn.close()

init_db()



r1 = LostReport(
    last_seen_date = "12-Oct-2026",
    report_id = 123,
    title = "Lost Bag", 
    description ="lost leather bag in mall near a shop", 
    category ="Bags", 
    location = "near Dr.Fixit", 
    date = "12-Oct-2026",
)


r2 = FoundReport(
    found_date = "18-Oct-2026",
    report_id = 123,
    title = "Lost Bag", 
    description ="lost leather bag in mall near a shop", 
    category ="Bags", 
    location = "near Dr.Fixit", 
    date = "12-Oct-2026"
)



# a = add_report(r1,1)
# b = add_report(r2,2)


# get_all_reports()