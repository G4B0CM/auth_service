class UserAlreadyExistsError(Exception):
    """Raised when a user with the given email already exists."""
    pass

class InvalidCredentialsError(Exception):
    """Raised when authentication fails due to incorrect credentials."""
    pass