from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Jumun(BaseModel):
    jmno : int
    userno  :int
    jpno :int
    size  :int
    price:int
    stack :int
    postcode :int
    addr : str
    phone :int

    class Config:
        from_attributes = True


