#!/usr/bin/python3
"""
module doc
"""

import sys
import MySQLdb as MQL


def main():
    """
    doc
    """
    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_host = "localhost"
    db_name = sys.argv[3]
    db_port = 3306
    try:
        conn = MQL.connect(host=db_host, port=db_port, user=db_user,
                           passwd=db_passwd, db=db_name, charset="utf8")
        cur = conn.cursor()
        cur.execute("SELECT cities.id, cities.name, states.name FROM cities \
                LEFT  JOIN states ON cities.state_id=states.id \
                ORDER BY cities.id ASC")
        content = cur.fetchall()
        for row in content:
            print(row)
        cur.close()
        conn.close()
    except Exception:
        raise
        pass


if __name__ == "__main__":
    main()
