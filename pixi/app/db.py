from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base


Base = declarative_base()
async_session = None
engine = None




def init_db(app):
global engine, async_session
engine = create_async_engine(app.config['DATABASE_URL'], echo=False, future=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)




# helper dependency
async def get_session():
async with async_session() as session:
yield session