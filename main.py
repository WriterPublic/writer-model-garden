import os
import uvicorn
import logging

if __name__ == "__main__":
    infer_port = int(os.environ.get("INFER_PORT"))
    logging.info(f"Inference port: {infer_port}")
    print(f"Inference port: {infer_port}")
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=infer_port,
        workers=1,
    )