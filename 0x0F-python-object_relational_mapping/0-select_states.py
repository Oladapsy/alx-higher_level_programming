#!/usr/bin/python3
''' a script that lists all states from the database hbtn_0e_0_usa '''
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv

    db = MySQLdb.connect(host=localhost, user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT `states` FROM hbtn_0e_0_usa ORDER BY states.id")
    rows = cur.fetchall()
    for items in rows:
        print(items)
