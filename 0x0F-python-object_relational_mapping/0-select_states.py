#!/usr/bin/python3
# """ a script that lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb

if __name__ == "__main__":
    args = []
    args = sys.argv
    db = MySQLdb.connect(port=3306, user=args[1], passwd=args[2], db=args[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    query_rows = cur.fetchall()
    for row in query_rows:
        [print(row)]
