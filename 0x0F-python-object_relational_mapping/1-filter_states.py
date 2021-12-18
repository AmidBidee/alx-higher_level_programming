#!/usr/bin/python3
"""
1-filter_states moudule
lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa:
"""


def filter_state(u: str, passwd: str, name: str):
    """
    lists states starting with 'N' from the database

    Args:
        u: str -> user to connect as
        passwd: str -> user password
        name: str -> database name

    Returns:
        None
    """

    # setup db connection
    host = 'localhost'
    db = MySQLdb.connect(host, u, passwd, name)
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
        print(elem, end='\n')


# executes srcipt
if __name__ == '__main__':
    import sys
    import MySQLdb

    lt = len(sys.argv)
    if lt >= 2:
        u, p, n = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_state(u, p, n)  # run function
