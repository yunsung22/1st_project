from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'product'

    prdno = Column(Integer, primary_key=True, autoincrement=True)
    prdname = Column(String(50), nullable=False, unique=True)
    category = Column(String(30), nullable=False)
    img = Column(String(100))
    stack = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    salepoint = Column(Float, default=0.0)
    regdate = Column(DateTime, default=datetime.now(), nullable=True) # 상품등록일
