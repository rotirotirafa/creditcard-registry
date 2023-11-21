from fastapi import APIRouter, Depends

UsersRouter = APIRouter(
    prefix='/users'
)


@UsersRouter.post("/create-account")
def create_user_account():
    pass

