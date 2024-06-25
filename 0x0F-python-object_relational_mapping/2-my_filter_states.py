#!/usr/bin/python3
"""takes argument and displays all values in the states table
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

    """execute query with given input"""
    query = (
            "SELECT * FROM states WHERE name = %s"
            "ORDER BY states.id ASC"
            )
    cursor.execute(query, (state_name_searched,))

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
