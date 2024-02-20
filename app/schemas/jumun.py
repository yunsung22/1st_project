from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Jumun(BaseModel):
    jmno: int
    userid: str  # 회원아이디
    addr: str  # 회원 주소
    prno: int  # 제품 번호
    price: int
    prdname: str  # 제품 이름
    stack: int  # 수량
    jumundate: datetime  # 주문 날짜
    email: str  # 이메일
    name: str  # 이름
    postalcode: str  # 우편번호
    phone: int  # 핸드폰 번호

class Config:
    from_attributes = True

class JumunAttach(BaseModel):
    jmano : int
    jmno :int
    fname : str
    fsize : int

    class Config:
        from_attributes = True


class NewJumun(BaseModel):
    prdname: str
    fname : str
    price: int
    stack: int

