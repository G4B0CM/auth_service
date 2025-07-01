from typing import Optional
from sqlalchemy.orm import Session
from app.application.interfaces.user_repository import AbstractUserRepository
from app.domain.models import UserInDB, UserCreate
from.models import UserDB

class PostgresUserRepository(AbstractUserRepository):
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_by_email(self, email: str) -> Optional:
        user_db = self.db.query(UserDB).filter(UserDB.email == email).first()
        if user_db:
            return UserInDB.from_orm(user_db)
        return None

    def add(self, user_create: UserCreate, hashed_password: str) -> UserInDB:
        db_user = UserDB(
            email=user_create.email,
            full_name=user_create.full_name,
            hashed_password=hashed_password
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return UserInDB.from_orm(db_user)