from datetime import datetime, timezone
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel, Field


class QueueItem(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid4()))
    user: str
    song_or_action: str
    weight: float = 1.0
    is_mod_approved: bool = False
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class QueueManager:
    def __init__(self) -> None:
        self._queue: list[QueueItem] = []

    def add_item(self, item: QueueItem) -> QueueItem:
        self._queue.append(item)
        return item

    def approve_item(self, item_id: str) -> Optional[QueueItem]:
        for item in self._queue:
            if item.id == item_id:
                item.is_mod_approved = True
                return item
        return None

    def get_queue(self) -> list[QueueItem]:
        return self._queue


queue_manager = QueueManager()
