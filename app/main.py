from fastapi import FastAPI
from app.api.routes_infer import router as infer_router

app = FastAPI(title="People Detection API")
app.include_router(infer_router)
