from .state import QueueItem


def validate_queue_item(item: QueueItem) -> bool:
    return bool(item.user.strip() and item.song_or_action.strip())
