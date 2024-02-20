from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Base(DeclarativeBase):
    pass

class Cart(Base):
    __tablename__ = 'cart'

    cno = Column(Integer, primary_key=True, autoincrement=True) #카트번호
    mno = mapped_column(Integer, nullable=False)
    jpno = Column(Integer, nullable=False)
    size = Column(String(20), nullable=False)
    qty = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
