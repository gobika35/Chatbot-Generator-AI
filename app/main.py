from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.api.generate_bot import router as generate_router
from app.api.preview_bot import router as preview_router
from app.api.update_theme import router as theme_router
from app.utils.logger import logger
from app.utils.rate_limit import rate_limiter

app = FastAPI(title="Chatbot Generator AI")

app.middleware("http")(rate_limiter)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"error": "Internal server error"}
    )

app.include_router(generate_router, prefix="/generate")
app.include_router(preview_router, prefix="/preview")
app.include_router(theme_router, prefix="/theme")

@app.get("/")
def root():
    return {"status": "ok"}
