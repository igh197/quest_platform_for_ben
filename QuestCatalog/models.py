import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String, Boolean, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

SQL_ADDRESS = f'mysql+pymysql://{os.environ["sql_db_user"]}:{os.environ["sql_db_password"]}@{os.environ["sql_db_address_pq"]}:{os.environ["sql_db_port"]}/{os.environ["sql_db_connect"]}'

engine = create_engine(
    SQL_ADDRESS
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Quests(Base):
    __tablename__ = 'quest'
    quest_id = Column(Integer, primary_key=True, index=True)
    auto_claim = Column(Boolean)
    streak = Column(Integer)
    duplication = Column(Integer)
    name = Column(String)
    owner_id = Column(Integer, ForeignKey("reward.reward_id"))
    owner = relationship("Reward", back_populates="quests")
    description = Column(String)


class Reward(Base):
    __tablename__ = 'reward'
    reward_id = Column(Integer, primary_key=True, index=True)
    reward_name = Column(String)
    reward_item = Column(String)
    reward_qty = Column(Integer)
    quests = relationship("Quests", back_populates="owner")


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
