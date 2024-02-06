import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, Float, DateTime, func, Sequence, Date, DECIMAL

class Base(DeclarativeBase):
    pass

class Member(Base):
    __tablename__ = 'member'

    mno = Column(Integer, primary_key=True, autoincrement=True)
    userid = Column(String(18), nullable=False, unique=True)
    passwd = Column(String(18), nullable=False)
    name = Column(String(10), nullable=False)
    email = Column(String(50), nullable=False)
    regdate = Column(DateTime, default=datetime.datetime.now(), nullable=True)