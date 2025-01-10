import os
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient

# Load environment variables from .env file
load_dotenv()

# MongoDB connection string
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB_NAME = os.getenv("MONGO_DB_NAME")

# Initialize MongoDB client
client = AsyncIOMotorClient(MONGO_URI)

# Access the database
db = client[MONGO_DB_NAME]
