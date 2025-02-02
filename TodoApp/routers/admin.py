from typing import Annotated

from starlette import status
from fastapi import  HTTPException,APIRouter
from fastapi.params import Depends
from sqlalchemy.orm import Session

from models import Todos
from database import sessionLocal
from routers.auth import get_current_user

router = APIRouter(
    prefix='/admin',
    tags=['admin']
)

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict,Depends(get_current_user)]




@router.get("/todo",status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency,db: db_dependency):
    if user is None or user.get('user_role')!='admin':
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail='Auth failed')
    return db.query(Todos).all()