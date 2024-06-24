#!/usr/bin/python3
""" lists all the states from the database hbtn_0e_0_usa."""

import MySQLdb
import sys


def states():
    """get command-line arguments."""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    """ Connect to MySQL server."""
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )

    """ cursor object to execute query"""
    cursor = db.cursor()

    """ execute sql query."""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """ fetch all results."""
    results = cursor.fetchall()

    """print results."""
    for row in results:
        print(row)

    cursor.close()
    """close cursor."""

    db.close()
    """close of database connection"""


if __name__ == "__main__":
    states()
