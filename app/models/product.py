from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'product'

    prdno = Column(Integer, primary_key=True, autoincrement=True)
    prdname = Column(String(50), nullable=False, unique=True)
    category = Column(String(30), nullable=False)
    stack = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    salepoint = Column(Float, default=0.0)
    contents = Column(Text, nullable=False)
    regdate = Column(DateTime, default=datetime.now(), nullable=True) # 상품등록일


class PrdAttach(Base):
    __tablename__ = 'prdattach'

    prdatno = Column(Integer, primary_key=True, autoincrement=True)
    prdno = mapped_column(Integer, ForeignKey('product.prdno'))
    img1 = Column(String(50), nullable=False)
    img2 = Column(String(50), nullable=False)
    img3 = Column(String(50), nullable=False)
    img4 = Column(String(50), nullable=False)

