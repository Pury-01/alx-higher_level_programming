#!/usr/bin/python3
"""lists all cities from database hbtn_0e_4_usa"""

import MySQLdb
import sys


def cities():
    """get command-line arguments"""
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
    """cursor object for sql query"""
    cursor = db.cursor()

    """sql query execution"""
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(query)

    """fetch all results"""
    results = cursor.fetchall()

    for row in results:
        print(row)

    """close cursor and database connection"""
    cursor.close()
    db.close()


if __name__ == "__main__":
    cities()
