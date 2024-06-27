#!/usr/bin/python3
"""displays all values in the states table where argument match
name.
"""

import MySQLdb
import sys


def states():
    """get command line arguments"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name_searched = sys.argv[4]

    """connect to MYSQL server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )

    """cursor object for query execution"""
    cursor = db.cursor()

    query = (
            "SELECT * FROM states WHERE name = %s"
            "ORDER BY states.id ASC"
            )
    """execute slq query"""
    cursor.execute(query, (state_name_searched,))

    """fetch all and print results"""
    results = cursor.fetchall()
    for row in results:
        print(row)

    cursor.close()
    """close cursor"""

    db.close()
    """close database connection"""


if __name__ == "__main__":
    states()
