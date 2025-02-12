# main.py
from fastapi import FastAPI
from assignments import assignments_router  # This router already has prefix "/assignments"
from auth import router as auth_router        # This router already has prefix "/auth"

app = FastAPI()

app.include_router(assignments_router)
app.include_router(auth_router)

@app.get("/")
async def root():
    return {"message": "FastAPI is working!"}
