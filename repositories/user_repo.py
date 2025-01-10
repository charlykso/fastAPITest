from typing import List
from db.database import db
from models.user import UserSchema
from helpers.convert_id import convert_id

class UserRepo:
    async def get_all(self) -> List[UserSchema]:
        results = await db["users"].find().to_list(length=100)
        return [convert_id(result) for result in results]