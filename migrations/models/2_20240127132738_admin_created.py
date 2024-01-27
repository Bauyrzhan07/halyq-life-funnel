from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "admin" (
    "id" BIGSERIAL NOT NULL PRIMARY KEY,
    "email" VARCHAR(200) NOT NULL  DEFAULT '',
    "username" VARCHAR(50) NOT NULL UNIQUE,
    "password" VARCHAR(200) NOT NULL,
    "last_login" TIMESTAMPTZ NOT NULL,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "admin";"""
