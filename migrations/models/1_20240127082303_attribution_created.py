from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "attribution" (
    "id" UUID NOT NULL  PRIMARY KEY,
    "created_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "updated_at" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP,
    "user_id" BIGINT,
    "gender" VARCHAR(6),
    "age" VARCHAR(6),
    "properties" JSONB NOT NULL
);
CREATE INDEX IF NOT EXISTS "idx_attribution_user_id_e0c147" ON "attribution" ("user_id");
COMMENT ON COLUMN "attribution"."gender" IS 'MALE: MALE\nFEMALE: FEMALE';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "attribution";"""
