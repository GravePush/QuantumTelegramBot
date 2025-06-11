import asyncio
import asyncpg

from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME


async def create_database():
    conn = await asyncpg.connect(
        user=DB_USER,
        password=DB_PASS,
        host=DB_HOST,
        port=DB_PORT,
        database='postgres'
    )
    dbs = await conn.fetch("SELECT 1 FROM pg_database WHERE datname=$1", DB_NAME)
    if not dbs:
        print(f"Создаём базу данных {DB_NAME}")
        await conn.execute(f'CREATE DATABASE "{DB_NAME}"')
    else:
        print(f"База данных {DB_NAME} уже существует.")
    await conn.close()


if __name__ == "__main__":
    asyncio.run(create_database())
