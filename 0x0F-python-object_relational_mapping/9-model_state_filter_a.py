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
        for state in session.query(State).filter(
                State.name.like('%a%')).order_by(State.id).all():
            print(f"{state.id}: {state.name}")
        session.close()
    except Exception:
        pass


if __name__ == "__main__":
    main()
