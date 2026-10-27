from .state import QueueItem


def reason_about_queue(item: QueueItem) -> dict:
    return {
        "status": "stub",
        "message": "Codex reasoning is not implemented yet.",
        "item_id": item.id,
    }
