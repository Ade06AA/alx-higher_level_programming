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
        cur.execute("SELECT * FROM states WHERE CONVERT(name USING \
                Latin1) COLLATE Latin1_General_CS LIKE 'N%'")
        content = cur.fetchall()
        for row in content:
            print(row)
    except Exception:
        raise
    finally:
        cur.close()
        conn.close()


if __name__ == "__main__":
    main()
