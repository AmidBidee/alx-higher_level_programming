#!/usr/bin/python3
"""
displays all values in the states table of
the database where name matches the argument.
"""
import sys
import MySQLdb


# executes srcipt
if __name__ == '__main__':

    user, passwd, db_name, search_string = (sys.argv[1],
                                            sys.argv[2],
                                            sys.argv[3],
                                            sys.argv[4])

    # setup db connection
    host = 'localhost'
    port = 3306
    db = MySQLdb.connect(host, user, passwd, db_name, port=port)
    cur = db.cursor()

    # query database
    query_string = """SELECT id, name
                    FROM states
                    WHERE name='{}'
                    ORDER BY id ASC""".format(search_string)
    cur.execute(query_string)

    # get and print results
    result = cur.fetchall()
    for elem in result:
        if elem[1] == search_string:
            print(elem, end='\n')

    cur.close()
    db.close()
