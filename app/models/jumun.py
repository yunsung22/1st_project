from datetime import datetime

from sqlalchemy import Column, Integer, String,  DateTime
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Jumun(Base):
    __tablename__ = 'jumun'

    jmno = Column(Integer,primary_key=True, autoincrement=True)
    userno = Column(Integer, nullable=False, unique=True)
    userloca = Column(String(50), nullable=False)
    prno = Column(Integer, nullable=False)
    quantity = Column(Integer,nullable=False, unique=True)
    jumundate = Column(DateTime, default=datetime.now )
