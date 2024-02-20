from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Base(DeclarativeBase):
    pass

class Member(Base):
    __tablename__ = 'member'

    mno = Column(Integer, primary_key=True, autoincrement=True) #회원번호
    userid = Column(String(50), nullable=False, unique=True) #고객아이디
    passwd = Column(String(50), nullable=False) #비밀번호
    name = Column(String(20), nullable=False)   #고객이름
    email = Column(String(50), nullable=False)  #이메일
    addr = Column(String(1000), nullable=False)  #회원주소
    birth = Column(String(10), nullable=False)  #생년월일
    phone = Column(String(11), nullable=False)  #핸드폰
    point = Column(Integer, default=0)  #적립금
    regdate = Column(DateTime, default=datetime.now(), nullable=True) #회원등록일


class User(Base):
    __tablename__ = 'user'

    userno = Column(Integer, primary_key=True, autoincrement=True)  # 사용자번호
    mno = mapped_column(Integer, ForeignKey('member.mno'))            # 회원번호 - 외래키
    usertype = Column(String(50), default='member')                 # 사용자유형(domain) - member, manager, admin
    regdate = Column(DateTime, default=datetime.now(), nullable=True)       # 회원등록일
    lastmodfidate = Column(DateTime, default=datetime.now(), nullable=True) # 회원수정일
