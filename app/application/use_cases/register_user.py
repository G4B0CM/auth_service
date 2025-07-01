from app.application.interfaces.user_repository import AbstractUserRepository
from app.domain.services import PasswordService
from app.domain.models import User
from app.application.dtos import UserCreateDTO
from app.domain.exceptions import UserAlreadyExistsError

class RegisterUserUseCase:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    def execute(self, user_dto: UserCreateDTO) -> User:
        existing_user = self.user_repo.get_by_email(user_dto.email)
        if existing_user:
            raise UserAlreadyExistsError("Email already registered")
        
        hashed_password = PasswordService.get_password_hash(user_dto.password)
        
        new_user_in_db = self.user_repo.add(user_dto, hashed_password)
        
        return User.from_orm(new_user_in_db)