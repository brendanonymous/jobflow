import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from collections.abc import Generator
from sqlalchemy.orm import Session, declarative_base, sessionmaker

load_dotenv()

DATABASE_URL = os.environ["DATABASE_URL"]

if DATABASE_URL is None:
    raise RuntimeError("DATABASE_URL is not set")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

Base = declarative_base()

def get_session() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield session