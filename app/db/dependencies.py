from typing import Generator
from sqlalchemy.orm.session import Session
from fastapi.requests import HTTPConnection

def get_db(connection: HTTPConnection) -> Generator[Session, None]:
    session = connection.app.state.db_session_factory()

    try:
        yield session
    finally:
        session.commit()
        session.close()
