from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'product'

    prdno = Column(Integer, primary_key=True, autoincrement=True)
    prdname = Column(String(18), nullable=False, unique=True)
    category = Column(DateTime, default=datetime.now)
    img = Column(String(100), unique=True)
    stack = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    salepoint = Column(Float, nullable=False, unique=True)
