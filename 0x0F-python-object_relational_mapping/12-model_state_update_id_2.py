#!/usr/bin/python3
"""
module
"""
from sys import argv
import sys
from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import Session


def main():
    """
    empty doc
    """
    db_user = argv[1]
    db_passwd = argv[2]
    db_name = argv[3]
    db_host = "localhost"

    try:
        mstr = f"mysql+mysqldb://{db_user}:{db_passwd}@{db_host}/{db_name}"
        engine = create_engine(mstr, pool_pre_ping=True)
        Base.metadata.create_all(engine)
        session = Session(engine)
        state = session.query(State).get(2)
        state.name = "New Mexico"
        session.commit()
        session.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
