from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class Jumun(Base):
    __tablename__ = 'jumun'

    jmno = Column(Integer, primary_key=True, autoincrement=True)  # 주문번호
    mno = Column(Integer,nullable=False)  # 회원아이디 (member 연동)
    prdno = Column(Integer, nullable=False)  # 회원 주소 (member 연동)
    size = Column(String(50), nullable=False)  # 가격 (product 연동)
    qty = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)  # 제품 번호 (product 연동)
    postcode = Column(String(10), nullable=False)
    addr = Column(String(100), nullable=False)
    phone = Column(String(15), nullable=False)
    regdate = Column(DateTime, default=datetime.now(), nullable=True)



