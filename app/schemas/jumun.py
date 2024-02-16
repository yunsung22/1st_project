from datetime import datetime

from pydantic import BaseModel

class Jumun(BaseModel):
    jmno = int
    userno = int
    userloca = str
    prno = int
    quantity = int
    jumundate = datetime

class Config:
    from_attributes = True


class NewJumun(BaseModel):
    userloca : str
    prno = int
    quantity = int
