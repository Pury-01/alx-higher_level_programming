#!/usr/bin/python3
""" lists all the states with a name starting with N."""

import MySQLdb
import sys


def states():
    """take commandline arguments"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """connect to MySQL server"""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )

    cursor = db.cursor()
    """cursor object to execute query"""

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%'")
    """execute sql query"""

    results = cursor.fetchall()
    """fetch all the results"""

    for row in results:
        """print the results"""
        print(row)

    cursor.close()
    """close cursor"""
    db.close()
    """disconnect from database"""


if __name__ == "__main__":
    states()
