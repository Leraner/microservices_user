import grpc
from google.protobuf import wrappers_pb2
from .handler import Handler

protos, services = grpc.protos_and_services("protos/user_protos.proto")


class UserService(services.UsersServicer, Handler):
    async def CreateUser(self, request, context):
        created_user = await self.create_user(
            name=request.name, surname=request.surname
        )

        response = protos.CreateUserResponse(
            user=protos.User(
                id=str(created_user.id),
                name=created_user.name,
                surname=created_user.surname,
                # NOTE: Learn this question
                # is_deleted=wrappers_pb2.BoolValue(value=True),
                # created_at=timestamp_pb2.Timestamp(new_user.created_at),
            )
        )
        return response

    async def GetUsers(self, request, context):
        result = await self.get_users()

        if result is None:
            raise Exception("No users at all")

        response = protos.GetUsersResponse(
            users=[
                protos.User(
                    id=str(user.id),
                    name=user.name,
                    surname=user.surname,
                )
                for user in result
            ]
        )

        return response

    async def GetUsersByIds(self, request, context):
        result = await self.get_users_by_ids(user_ids=request.ids)

        if result is None:
            raise Exception(f"No users at all by ids: {request.ids}")

        response = protos.GetUsersByIdsResponse(
            users=[
                protos.User(
                    id=str(user.id),
                    name=user.name,
                    surname=user.surname,
                )
                for user in result
            ]
        )
        return response

    async def GetUserById(self, request, context):
        result = await self.get_user_by_id(user_id=request.id)

        if result is None:
            raise Exception(f"No user with id: {request.id}")

        response = protos.GetUserByIdResponse(
            user=protos.User(
                id=str(result.id),
                name=result.name,
                surname=result.surname,
            )
        )
        return response

    async def DeleteUser(self, request, context):
        deleted_user = await self.delete_user(user_id=request.id)

        if deleted_user is None:
            raise Exception(f"User not found with id '{request.id}'")

        response = protos.DeleteUserResponse(
            user=protos.User(
                id=str(deleted_user.id),
                name=deleted_user.name,
                surname=deleted_user.surname,
            )
        )
        return response
