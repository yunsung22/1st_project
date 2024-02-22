from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Jumun(BaseModel):
    jmno : int
    mno  :int
    prdno :int
    size  :str
    price:int
    qty :int
    postcode :str
    addr : str
    phone :str
    regdate: datetime

    class Config:
        from_attributes = True


class NewJumun(BaseModel):
    mno  :int
    cno  :int
    prdno :int
    size  :str
    price:int
    qty :int
    postcode :str
    addr : str
    phone :str

