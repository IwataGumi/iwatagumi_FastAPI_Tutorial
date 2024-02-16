from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./fastapi_app.db"


def setup_db(app: FastAPI) -> None:
    engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
    session_factory: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    app.state.db_engine = engine
    app.state.db_session_factory = session_factory
