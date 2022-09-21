import sqlite3

def createdb():

    con = sqlite3.connect(database=r'ims.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(id INTEGER PRIMARY KEY AUTOINCREMENT, Name text , Phone TEXT , Email TEXT , Gender TEXT , Department TEXT , Adress TEXT , Salary INTEGER )")


createdb()

