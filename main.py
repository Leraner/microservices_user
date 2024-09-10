import asyncio
import os
from server import run_server


if __name__ == "__main__":
    os.system(
        "python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./protos/*.proto"
    )


    asyncio.run(run_server())
