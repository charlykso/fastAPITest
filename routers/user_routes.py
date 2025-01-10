from fastapi import APIRouter
from views import user_views
from models.user import UserSchema

router = APIRouter()

@router.get('/user/all')
async def get_all_users():
    return await user_views.get_all()

@router.get('/user/{user_id}')
async def get_user(user_id: int):
    return await user_views.get(user_id)

@router.post('/user')
async def create_user(user: UserSchema):
    await user_views.create(user)

