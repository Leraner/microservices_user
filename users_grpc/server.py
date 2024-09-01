import grpc
from .users import UserService

protos, services = grpc.protos_and_services("user_protos/user_protos.proto")


async def run_server():
    server = grpc.aio.server()
    services.add_UsersServicer_to_server(UserService(), server)
    server.add_insecure_port("0.0.0.0:50051")
    print("Service started on 0.0.0.0:50051")
    await server.start()
    await server.wait_for_termination()
