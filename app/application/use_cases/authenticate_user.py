from app.application.interfaces.user_repository import AbstractUserRepository
from app.domain.services import PasswordService
from app.infrastructure.security.jwt_handler import JWTHandler
from app.domain.models import Token
from app.domain.exceptions import InvalidCredentialsError

class AuthenticateUserUseCase:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    def execute(self, email: str, password: str) -> Token:
        user = self.user_repo.get_by_email(email)
        if not user or not PasswordService.verify_password(password, user.hashed_password):
            raise InvalidCredentialsError("Incorrect email or password")
        
        access_token = JWTHandler.create_access_token(data={"sub": user.email})
        
        return Token(access_token=access_token, token_type="bearer")