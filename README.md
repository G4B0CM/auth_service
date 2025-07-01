# Authentication Service
## Overview
The Authentication Service is a core component of the Risk Assessment Platform. It is responsible for managing user identities, handling user registration and login, and issuing JSON Web Tokens (JWTs) for securing API endpoints across the entire microservice ecosystem.

## Core Responsibilities
User Registration: Allows new users to create an account. Passwords are securely hashed before being stored.
User Authentication: Validates user credentials (email and password) and issues a JWT access token upon successful login.
Token Management: Provides mechanisms for creating and decoding JWTs, which will be used by the API Gateway (Kong) and other services to authorize requests.

## Tech Stack
Language: Python 3.11+
Framework: FastAPI
Data Validation: Pydantic
Password Hashing: Passlib with bcrypt
JWT Handling: python-jose
Database ORM: SQLAlchemy
Database: PostgreSQL

## Running the Service
Set up Environment Variables:
Copy the .env.example file to .env and fill in the required values:bash
cp.env.example.env


## Build and Run with Docker:
docker build -t auth-service.
docker run -p 8000:8000 --env-file.env auth-service

## API Documentation:
Once running, the interactive API documentation (Swagger UI) will be available at http://localhost:8000/docs.


---

#### **File: `risk_assessment_platform/services/auth_service/Dockerfile`**
```dockerfile
# Stage 1: Build stage with development dependencies
FROM python:3.11-slim as builder

WORKDIR /app

# Install poetry for dependency management
RUN pip install poetry

# Copy only the dependency definition files
COPY poetry.lock pyproject.toml./

# Install dependencies, but not the project itself, into a virtual environment
# --no-root: Don't install the project itself
# --no-dev: Exclude development dependencies like pytest
RUN poetry config virtualenvs.in-project true && \
    poetry install --no-root --no-dev

# Stage 2: Final production stage
FROM python:3.11-slim

WORKDIR /app

# Copy the virtual environment from the builder stage
COPY --from=builder /app/.venv./.venv

# Activate the virtual environment
ENV PATH="/app/.venv/bin:$PATH"

# Copy the application code
COPY./app./app

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application using Uvicorn
# --host 0.0.0.0 makes it accessible from outside the container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]