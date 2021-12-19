#!/usr/bin/python3
"""
1-filter_states moudule
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
"""
import sys
import MySQLdb


# executes srcipt
if __name__ == '__main__':

    u, passwd, name = sys.argv[1], sys.argv[2], sys.argv[3]

    # setup db connection
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(host, u, passwd, name, port=port)
    cur = db.cursor()

    # query database
    query_string = """ SELECT id, name
                        FROM states
                        WHERE name LIKE 'N%'
                        ORDER BY id ASC"""
    cur.execute(query_string)

    # get and print results
    result = cur.fetchall()
    for elem in result:
        if elem[1][0] == 'N':
            print(elem, end='\n')

    cur.close()
    db.close()
