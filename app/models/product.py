from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Float, Text, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass

class Product(Base):
    __tablename__ = 'product'

    prdno = Column(Integer, primary_key=True, autoincrement=True)
    prdname = Column(String(18), nullable=False, unique=True)
    contents = Column(Text, nullable=False)
    category = Column(DateTime, default=datetime.now)
    img = Column(String(100), unique=True)
    stack = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    salepoint = Column(Float, nullable=True)

class GalAttach(Base):
    __tablename__ = 'galattach'

    pno= Column(Integer, primary_key=True, autoincrement=True)
    prdno= mapped_column(Integer, ForeignKey('product.prdno'))
    fname = Column(String(50), nullable=False)
    fsize = Column(Integer, default=0)