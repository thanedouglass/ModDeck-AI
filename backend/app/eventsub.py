from fastapi import APIRouter, Request

router = APIRouter(prefix="/eventsub", tags=["eventsub"])


@router.post("/verify")
async def verify_webhook(request: Request) -> dict:
    payload = await request.json()
    return {"status": "received", "challenge": payload.get("challenge")}


@router.post("/event")
async def handle_event(_: Request) -> dict:
    return {"status": "ok"}
