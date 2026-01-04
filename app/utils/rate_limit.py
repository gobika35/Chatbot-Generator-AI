import time
from fastapi import Request
from fastapi.responses import JSONResponse

REQUEST_LIMIT = 60
WINDOW = 60  # seconds

_clients = {}

async def rate_limiter(request: Request, call_next):
    ip = request.client.host
    now = time.time()

    history = _clients.get(ip, [])
    history = [t for t in history if now - t < WINDOW]

    if len(history) >= REQUEST_LIMIT:
        return JSONResponse(
            status_code=429,
            content={"error": "Too many requests"}
        )

    history.append(now)
    _clients[ip] = history

    return await call_next(request)
