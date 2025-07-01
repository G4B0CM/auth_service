from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.domain.models import User, Token
from app.application.dtos import UserCreateDTO
from app.application.use_cases.register_user import RegisterUserUseCase
from app.application.use_cases.authenticate_user import AuthenticateUserUseCase
from app.application.interfaces.user_repository import AbstractUserRepository
from app.domain.exceptions import UserAlreadyExistsError, InvalidCredentialsError
from app.presentation.api.deps import get_user_repository

router = APIRouter()

@router.post("/register", response_model=User, status_code=status.HTTP_201_CREATED)
def register_user(
    user_in: UserCreateDTO,
    user_repo: AbstractUserRepository = Depends(get_user_repository)
):
    try:
        use_case = RegisterUserUseCase(user_repo)
        user = use_case.execute(user_in)
        return user
    except UserAlreadyExistsError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )

@router.post("/token", response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_repo: AbstractUserRepository = Depends(get_user_repository)
):
    try:
        use_case = AuthenticateUserUseCase(user_repo)
        token = use_case.execute(email=form_data.username, password=form_data.password)
        return token
    except InvalidCredentialsError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )