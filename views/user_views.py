from fastapi import HTTPException
from models.user import UserSchema, UserResponseSchema
from  helpers.password_data import hash_password
from db.database import db
from typing import List
from repositories.user_repo import UserRepo
from helpers.convert_id import convert_id

async def get(user_id: int):
    try:
        user = await UserSchema.find_one({"_id": user_id})
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        return user
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

async def get_all()-> List[UserResponseSchema]:
    return await UserSchema.get_all()

async def create(user: UserSchema):
    try:
        user.password = hash_password(user.password)
        user_data = user.model_dump()
        # Save user to the database
        result = await db["users"].insert_one(user_data)
        print(result)
        return {"id": convert_id(result.inserted_id), "message": "User created successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")