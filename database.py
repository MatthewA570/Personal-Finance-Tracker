import sqlite3


def initialize_database():

    datab = sqlite3.connect("data.db")
    curse = datab.cursor()

    table = ("""CREATE TABLE IF NOT EXISTS record_book(
            ID INTEGER PRIMARY KEY,
            NAME TEXT, 
            CATEGORY TEXT,
            COST REAL,
            DATE FLOAT);""")
    
    curse.execute(table)
    datab.commit()
    curse.close()
    datab.close()


def new_Connection():
    datab = sqlite3.connect("data.db")
    datab.execute("PRAGMA foreign_keys = ON;")
    datab.row_factory = sqlite3.Row
    return datab







