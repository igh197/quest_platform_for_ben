import os

from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))

SQL_ADDRESS = f'mysql+pymysql://{os.environ["sql_db_user"]}:{os.environ["sql_db_password"]}@{os.environ["sql_db_address"]}:{os.environ["sql_db_port"]}/{os.environ["sql_db_connect"]}'

engine = create_engine(
    SQL_ADDRESS
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, unique=True)

    password = Column(String)

    gold = Column(Integer)

    diamond = Column(Integer)
    status = Column(Integer) # not_new=1, new=0, banned=-1
    login_trial = Column(Integer,default=0)


def create_db_and_tables():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
