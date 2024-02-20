from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime

class Base(DeclarativeBase):
    pass

class Bag(Base):
    __tablename__ = 'bag'

    bno = Column(Integer, primary_key=True, autoincrement=True) #회원번호
    jpno = Column(Integer, nullable=False)
    jpname = Column(String(50), nullable=False)
    size = Column(String(20), nullable=False)
    price = Column(Integer, nullable=False)
    stack = Column(Integer, nullable=False)
