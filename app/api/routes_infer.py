from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
from app.services.interface_service import InferenceService

router = APIRouter(prefix="/infer", tags=["Inference"])


@router.post("/raw")
async def infer_raw(file: UploadFile = File(...)):
    data = await InferenceService.run_inference(file)
    return JSONResponse(content=data)


@router.post("/processed")
async def infer_processed(file: UploadFile = File(...)):
    data = await InferenceService.run_processed(file)
    return JSONResponse(content=data)
