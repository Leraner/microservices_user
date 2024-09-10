import grpc
from users_grpc.users import UserService
from settings import microservices

protos, services = grpc.protos_and_services("protos/user_protos.proto")


async def run_server():
    server = grpc.aio.server()
    services.add_UsersServicer_to_server(UserService(), server)
    address = microservices["user"]["address"]
    server.add_insecure_port(address)
    print("Service started on 0.0.0.0:50051")
    await server.start()
    await server.wait_for_termination()
