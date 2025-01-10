from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from db.database import db
from bson import ObjectId
from helpers.convert_id import convert_id
from pymongo import ASCENDING, DESCENDING

class UserSchema(BaseModel):
    firstname: str
    lastname: str
    email: str
    password: str
    phone: str
    is_active: bool = True
    is_admin: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    @classmethod
    async def get_all(cls) -> List["UserResponseSchema"]: 
        results = await db["users"].find().sort("created_at", DESCENDING).to_list(length=100)
        return [convert_id(result) for result in results]

class UserResponseSchema(BaseModel):
    id: str = Field(..., alias="_id")
    firstname: str
    lastname: str
    email: str
    password: str
    phone: str
    is_active: bool = True
    is_admin: bool = False
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
