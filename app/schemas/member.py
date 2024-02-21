from datetime import datetime

from pydantic import BaseModel

class Member(BaseModel):
    mno: int
    userid: str
    passwd: str
    name: str
    email: str
    addr: str
    birth: str
    phone: str
    regdate: datetime

class Config:
    from_attributes = True


class NewMember(BaseModel):
    userid: str
    passwd: str
    name: str
    email: str
    addr: str
    birth: str
    phone: str

class ModifyMember(BaseModel):
    passwd: str
    name: str
    email: str
    addr: str
    birth: str
    phone: str


class User(BaseModel):
    userno: int
    mno: int
    usertype: str
    regdate: datetime
    lastmodifidate: datetime

    class Config:
        from_attributes = True

class TempMember(BaseModel):
    userid: str
    email: str
    birth: str
    phone: str

