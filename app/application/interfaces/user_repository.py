from abc import ABC, abstractmethod
from typing import Optional
from app.domain.models import UserInDB, UserCreate

class AbstractUserRepository(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> Optional:
        raise NotImplementedError

    @abstractmethod
    def add(self, user_create: UserCreate, hashed_password: str) -> UserInDB:
        raise NotImplementedError