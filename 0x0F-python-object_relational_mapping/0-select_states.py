#!/usr/bin/python3
"""
0-select_states module
"""


def select_states(u: str, passwd: str, name: str):
    """
    prints list of all states in a database

    Args:
        [u:str]: username to connect as
        [passwd:str]: users password
        [name:str]: database name to connect to

    Return:
        None
    """

    # setup my connection and query
    host = "localhost"
    port = 3306
    order_field = "id"
    query_string = f"""SELECT * FROM states ORDER BY {order_field} ASC"""
    db = MySQLdb.connect(host, u, passwd, name)

    # get cursor and execute query
    cur = db.cursor()
    cur.execute(query_string)
    result = cur.fetchall()

    # print results in human readable form
    for row in result:
        print(row, end='\n')


if __name__ == '__main__':
    import MySQLdb
    import sys

    lt = len(sys.argv)
    if lt >= 2:
        u, p, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    select_states(u, p, db_name)
