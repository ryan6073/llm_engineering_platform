import os
import sys
import argparse
import uvicorn
from vllm.engine.arg_utils import AsyncEngineArgs
from vllm.entrypoints.openai.api_server import build_app

# --- Configuration Parameters ---
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_RELATIVE_PATH = "../../models/modelscope/Qwen/Qwen3-8B" # <--- Double-check this path
MODEL_PATH = os.path.abspath(os.path.join(CURRENT_DIR, MODEL_RELATIVE_PATH))

HOST = "0.0.0.0"
PORT = 8000
TRUST_REMOTE_CODE = True
TENSOR_PARALLEL_SIZE = 1 # Adjust based on your GPU count, e.g., 2

def start_vllm_server():
    print(f"Preparing to start vLLM server...")
    print(f"Model path: {MODEL_PATH}")
    print(f"Listening address: {HOST}:{PORT}")

    # 1. Build AsyncEngineArgs object
    # We will pass only the essential arguments that are almost certainly present.
    # If the error persists, it means 'build_app' itself is trying to use this attribute.
    engine_args = AsyncEngineArgs(
        model=MODEL_PATH,
        tokenizer=MODEL_PATH, # Tokenizer path is usually the same as model path
        trust_remote_code=TRUST_REMOTE_CODE,
        tensor_parallel_size=TENSOR_PARALLEL_SIZE,
        # Remove any other parameters if they are not explicitly supported by your vLLM version.
        # e.g., if 'gpu_memory_utilization' or 'max_model_len' were added and caused issues, remove them too.
    )

    # 2. Build FastAPI application
    app = build_app(engine_args)

    # 3. Run FastAPI application using uvicorn
    print(f"vLLM server starting at {HOST}:{PORT}...")
    uvicorn.run(app, host=HOST, port=PORT, log_level="info")

if __name__ == "__main__":
    if not os.path.exists(MODEL_PATH) or not os.path.isdir(MODEL_PATH):
        print(f"Error: Model path does not exist or is not a directory: {MODEL_PATH}")
        print("Please ensure the model is correctly downloaded to the specified directory and MODEL_PATH is accurate.")
        sys.exit(1)

    try:
        start_vllm_server()
    except Exception as e:
        print(f"An error occurred while starting the vLLM server: {e}")