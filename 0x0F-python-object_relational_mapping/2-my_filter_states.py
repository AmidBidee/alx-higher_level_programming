#!/usr/bin/python3
"""
displays all values in the states table of
the database where name matches the argument.
"""


def search_state(u: str, passwd: str, name: str, search_string: str):
    """
    prints the name value that matches the argument inputed

    Args:
        u: str -> user to connect as
        passwd: str -> user password
        name: str -> database name
        search: str -> search argument

    Returns:
        None
    """

    # setup db connection
    host = 'localhost'
    db = MySQLdb.connect(host, u, passwd, name)
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
        print(elem, end='\n')

    cur.close()
    db.close()


# executes srcipt
if __name__ == '__main__':
    import sys
    import MySQLdb

    lt = len(sys.argv)
    u, p, n, s = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    search_state(u, p, n, s)  # run function
