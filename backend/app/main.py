from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .eventsub import router as eventsub_router
from .state import queue_manager

app = FastAPI(title="ModDeck-AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(eventsub_router)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.get("/api/queue")
def get_queue() -> list[dict]:
    return [item.model_dump(mode="json") for item in queue_manager.get_queue()]
