#!/usr/bin/python3
"""lists all cities of a state using hbtn_0e_4_usa."""
import MySQLdb
import sys


def cities():
    """take command line arguments"""
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    """Connect to database"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=database_name
            )
    """create cursor"""
    cursor = db.cursor()

    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))
    """execute query"""

    """fetch alll the results"""
    results = cursor.fetchall()

    """print results"""
    print(",".join([row[0] for row in results]))

    """close cursor"""
    cursor.close()

    """close database"""
    db.close()


if __name__ == "__main__":
    cities()
