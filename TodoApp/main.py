
from fastapi import FastAPI


from routers import auth,todos,admin
import models

from database import engine

app = FastAPI()
# the below command would not run only if the todosapp.db file is not present in the project
models.Base.metadata.create_all(bind=engine)
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)