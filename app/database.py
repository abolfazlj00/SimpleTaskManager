from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URL, DATABASE_ECHO

engine = create_async_engine(
    DATABASE_URL,
    echo=DATABASE_ECHO
)
AsyncSessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

# Dependency
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
