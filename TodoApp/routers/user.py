from typing import Annotated

from pydantic import BaseModel, Field
from starlette import status
from fastapi import  HTTPException,APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from passlib.context import CryptContext
from database import sessionLocal
from routers.auth import get_current_user

router = APIRouter(
    prefix='/user',
    tags=['user']
)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()


class PasswordChangeRequest(BaseModel):
    password:str
    hashed_password:str = Field(min_length=6)

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# @router.get("/user",status_code=status.HTTP_200_OK)
# async def