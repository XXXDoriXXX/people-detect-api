import tempfile
from app.core.interface_client import CLIENT, MODEL_ID
from app.models.interface_dto import InferenceResultDTO


class InferenceService:
    @staticmethod
    async def run_inference(file) -> dict:

        with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmp:
            content = await file.read()
            tmp.write(content)
            tmp_path = tmp.name
        return CLIENT.infer(tmp_path, model_id=MODEL_ID)

    @staticmethod
    async def run_processed(file) -> dict:

        raw = await InferenceService.run_inference(file)
        result = InferenceResultDTO(**raw)
        return result.summary()
