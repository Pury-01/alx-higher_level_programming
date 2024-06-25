#!/usr/bin/python3
"""
Takes argument and displays all values in the states table
where name matches the argument.
"""

import MySQLdb
import sys


def states():
    """take command line arguments."""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    """connect to MySQL server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )
    """cursor object to query mysql"""
    cursor = db.cursor()

    """create sql query with format"""
    query = (
            "SELECT * FROM states WHERE name = '{}'"
            "ORDER BY states.id ASC".format(state_name_searched)
            )

    """Execute query"""
    cursor.execute(query)

    """fetch all the results"""
    results = cursor.fetchall()

    """print results"""
    for row in results:
        print(row)

    """close cursor"""
    cursor.close()

    """close database connection"""
    db.close()


if __name__ == "__main__":
    states()
