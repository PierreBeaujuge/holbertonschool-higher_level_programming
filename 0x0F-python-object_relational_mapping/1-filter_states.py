#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N) from the
database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
