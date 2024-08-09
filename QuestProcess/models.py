import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, Enum, Column, Date, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

SQL_ADDRESS = f'mysql+pymysql://{os.environ["sql_db_user"]}:{os.environ["sql_db_password"]}@{os.environ["sql_db_address_p"]}:{os.environ["sql_db_port"]}/{os.environ["sql_db_connect"]}'

engine = create_engine(
    SQL_ADDRESS
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class UserQuestReward(Base):
    __tablename__ = "user_quest_rewards"
    uqr_id = Column(Integer, primary_key=True, index=True)
    status = Column(String)
    date = Column(Date)
    user_id=Column(Integer)
    quest_id=Column(Integer)


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
