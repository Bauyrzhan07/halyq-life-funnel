from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "product" ADD "min_premium_amount" INT NOT NULL  DEFAULT 0;
        ALTER TABLE "product" ADD "max_insurance_coverage" INT NOT NULL  DEFAULT 10000000;
        ALTER TABLE "product" ADD "max_premium_amount" INT NOT NULL  DEFAULT 0;
        ALTER TABLE "product" ADD "duration_in_years" INT NOT NULL  DEFAULT 1;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE "product" DROP COLUMN "min_premium_amount";
        ALTER TABLE "product" DROP COLUMN "max_insurance_coverage";
        ALTER TABLE "product" DROP COLUMN "max_premium_amount";
        ALTER TABLE "product" DROP COLUMN "duration_in_years";"""
