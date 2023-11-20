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
    db_var = sys.argv[4]
    try:
        conn = MQL.connect(host=db_host, port=db_port, user=db_user,
                           passwd=db_passwd, db=db_name, charset="utf8")
        cur = conn.cursor()
        cur.execute(f"SELECT cities.name FROM cities LEFT JOIN states ON\
                cities.state_id=states.id WHERE states.name \
                = %s ORDER BY cities.id ASC", (db_var,))
        content = cur.fetchall()
        for row in content[:-1]:
            print(row[0], end=", ")
        print(content[-1][0])
        cur.close()
        conn.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
