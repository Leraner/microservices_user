import grpc
from google.protobuf import wrappers_pb2
from sqlalchemy import select, delete

from db.engine import async_session
from db.models import User

protos, services = grpc.protos_and_services("user_protos/user_protos.proto")


class UserService(services.UsersServicer):
    async def CreateUser(self, request, context):
        async with async_session() as session:
            async with session.begin():
                new_user = User(name=request.name, surname=request.surname)
                session.add(new_user)
                await session.flush()
                await session.refresh(new_user)
                response = protos.CreateUserResponse(
                    user=protos.User(
                        id=str(new_user.id),
                        name=new_user.name,
                        surname=new_user.surname,
                        is_deleted=wrappers_pb2.BoolValue(value=True),
                        # is_deleted=wrappers_pb2.BoolValue(value=bool(new_user.is_deleted)),
                        # created_at=timestamp_pb2.Timestamp(new_user.created_at),
                    )
                )
                return response

    async def GetUsers(self, request, context):
        async with async_session() as session:
            async with session.begin():
                users = await session.execute(select(User))
                fetched_users = users.scalars().all()
                response = protos.GetUsersResponse(
                    users=[
                        protos.User(
                            id=str(user.id), name=user.name, surname=user.surname
                        )
                        for user in fetched_users
                    ]
                )

                return response

    async def DeleteUser(self, request, context):
        async with async_session() as session:
            async with session.begin():
                result = await session.execute(
                    delete(User).where(User.id == request.id).returning(User)
                )
                await session.commit()
                deleted_user = result.fetchone()

                if deleted_user is None:
                    raise Exception(f"User not found with id '{request.id}'")

                response = protos.DeleteUserResponse(
                    user=protos.User(
                        id=str(deleted_user[0].id),
                        name=deleted_user[0].name,
                        surname=deleted_user[0].surname,
                    )
                )
                return response
