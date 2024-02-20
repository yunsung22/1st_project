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
    userid = Column(Integer,nullable=False)  # 회원아이디 가져올것
    addr = Column(String(500), nullable=False)  # 회원 주소 가져올것
    prno = Column(Integer, nullable=False)  # 제품 번호 가져올것
    price = Column(Integer, nullable=False)  # 가격
    prdname = Column(String(50), nullable=False)  # 제품 이름 가져올것
    stack = Column(Integer, nullable=False)  # 수량 가져올것
    jumundate = Column(DateTime, default=datetime.now)  # 주문 날짜
    email = Column(String(50), nullable=False)  # 이메일 가져올것
    name = Column(String(50), nullable=False)  # 이름 가져올것
    postalcode = Column(Integer, nullable=False)  # 우편번호 가져올것
    phone = Column(Integer, nullable=False)  # 핸드폰 번호 가져올것


class JumunAttach(Base):
    __tablename__ = 'jumunattach'

    jmano = Column(Integer, primary_key=True, autoincrement=True)
    jmno = mapped_column(Integer, ForeignKey('jumun.jmno'))
    fname = Column(String(50), nullable=False)
    fsize = Column(Integer, default=0)

