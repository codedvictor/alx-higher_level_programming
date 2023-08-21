#!/usr/bin/python3
"""
Filter all states starting with N using mysqldb
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    dbs = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                          passwd=argv[2], db=argv[3])

    cur = dbs.cursor()
    cur.execute("""SELECT * FROM states
                   WHERE name = %s
                   ORDER BY id ASC;
                   """, (argv[4], ))
    states = cur.fetchall()

    for state in states:
        print(state)
