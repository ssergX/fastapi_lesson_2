from fastapi import APIRouter

tasks = APIRouter(prefix="/task", tags=["task"])


@tasks.get("/")
async def all_tasks():
    {"task": "all tasks"}
