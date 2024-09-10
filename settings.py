import os

DB_NAME = os.getenv("DB_NAME", "postgres")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "0.0.0.0")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_DIALECT = os.getenv("DB_DIALECT", "postgresql")
DB_DRIVER = os.getenv("DB_DRIVER", "asyncpg")


DATABASE_URL = (
    f"{DB_DIALECT}+{DB_DRIVER}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


microservices = {
    "user": {
        "address": "0.0.0.0:50051",
        "path_to_proto": "protos/user_protos.proto",
    },
    "post": {
        "address": "0.0.0.0:50052",
        "path_to_proto": "protos/post_protos.proto",
    },
}
