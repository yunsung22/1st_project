from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime

class Base(DeclarativeBase):
    pass

class Customer_Inquiry(Base):
    __tablename__ = 'customer_inquiries'
    id = Column(Integer, primary_key=True)
    customer_number = Column(Integer, autoincrement=True)  #외래키 사용해야함
    title = Column(String(50),nullable=False)
    content = Column(Text, nullable=False)
    inquiry_number = Column(Integer, autoincrement=True)
    regdate = Column(DateTime, default=datetime.now)

