from fastapi import FastAPI
from app.api.generate_bot import router as generate_router
from app.api.preview_bot import router as preview_router
from app.api.update_theme import router as theme_router
from app.config import settings

app = FastAPI(title=settings.APP_NAME)

app.include_router(generate_router, prefix="/generate", tags=["Generate"])
app.include_router(preview_router, prefix="/preview", tags=["Preview"])
app.include_router(theme_router, prefix="/theme", tags=["Theme"])

@app.get("/")
def root():
    return {"status": "running", "app": settings.APP_NAME}
