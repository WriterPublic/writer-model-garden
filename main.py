import os
import uvicorn

if __name__ == "__main__":
    infer_port = os.environ.get("INFER_PORT", 7080)
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=infer_port,
        workers=1,
    )