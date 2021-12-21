#!/usr/bin/python3
"""
lists all cities from the database
"""
import sys
import MySQLdb

if __name__ == '__main__':

    host = 'localhost'
    port = 3306
    u, passwd, db_name, search = (sys.argv[1],
                                  sys.argv[2],
                                  sys.argv[3],
                                  sys.argv[4])

    # connect to db
    db = MySQLdb.connect(host, u, passwd, db_name, port=port)
    cur = db.cursor()

    # query db
    query_string = """SELECT cities.name
                        FROM states
                        INNER JOIN cities ON states.id = cities.state_id
                        WHERE states.name = '{}'
                        ORDER BY cities.id ASC""".format(search)
    cur.execute(query_string)

    # print result
    results = cur.fetchall()

    rl = len(results)
    if rl:
        for row in results:
            if results.index(row) != (rl-1):
                print(row[0], end=', ')
            else:
                print(row[0])
    else:
        print()

    # close db and connection
    cur.close()
    db.close()
