from datetime import datetime

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import DeclarativeBase, mapped_column

class Base(DeclarativeBase):
    pass

class Jumun(Base):
    __tablename__ = 'jumun'

    jmno = Column(Integer, primary_key=True, autoincrement=True)  # 주문번호
    userno = mapped_column(Integer,ForeignKey('member.mno'),nullable=False)  # 회원아이디 (member 연동)
    jpno = mapped_column(Integer, ForeignKey('product.prdno'),nullable=False)  # 회원 주소 (member 연동)
    # size = Column(String(50), nullable=False)  # 가격 (product 연동)
    # price = Column(Integer, nullable=False)  # 제품 번호 (product 연동)
    # stack = Column(Integer, nullable=False)
    postcode = Column(Integer, nullable=False)
    # addr = Column(String(100), nullable=False)
    # phone = Column(Integer, nullable=False)
    regdate = Column(DateTime, default=datetime.now(), nullable=True)



