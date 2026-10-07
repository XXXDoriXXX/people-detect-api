import os

from inference_sdk import InferenceHTTPClient

API_KEY = os.environ.get("ROBOFLOW_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "ROBOFLOW_API_KEY is not set. Set it in the environment (see .env.example)."
    )

CLIENT = InferenceHTTPClient(
    api_url="https://serverless.roboflow.com",
    api_key=API_KEY,
)

MODEL_ID = "people-detection-o4rdr/11"
