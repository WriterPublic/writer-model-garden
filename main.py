import os
import uvicorn

if __name__ == "__main__":
    print("env variable passed: ", os.environ.get("DUMMY"))
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=5000,
        workers=1,
    )