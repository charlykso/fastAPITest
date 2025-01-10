from fastapi import FastAPI
from routers import user_routes

app = FastAPI()

app.include_router(user_routes.router, prefix="/api/v1")


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
