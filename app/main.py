from fastapi import FastAPI
from app.core.config import settings
from app.presentation.api.v1.router import api_router
from app.infrastructure.database.models import Base
from app.infrastructure.database.session import engine

# This line creates the database tables if they don't exist.
# In a real production environment, you would use a migration tool like Alembic.
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG_MODE,
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/", tags=)
def read_root():
    return {"message": f"Welcome to the {settings.APP_NAME}"}