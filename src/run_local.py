import os
import uvicorn


if __name__ == "__main__":
    uvicorn.run(
        "src.main:app",
        host="127.0.0.1",
        port=5080,
        reload=True,
        log_level="debug",
    )
