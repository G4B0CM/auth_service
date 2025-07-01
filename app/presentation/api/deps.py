from typing import Generator
from sqlalchemy.orm import Session
from app.infrastructure.database.session import SessionLocal
from app.infrastructure.database.repositories import PostgresUserRepository
from app.application.interfaces.user_repository import AbstractUserRepository

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_user_repository(db: Session = next(get_db())) -> AbstractUserRepository:
    return PostgresUserRepository(db)