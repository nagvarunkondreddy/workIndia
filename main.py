from fastapi import FastAPI
from routers import user
app = FastAPI(
    title="workindia-api",
    description="Backend",
    version="1.0"
)


app.include_router(
    user.router,
    prefix="/user",
    tags=["User"]
)

if __name__ == "__main__":
    uvicorn.run(app)