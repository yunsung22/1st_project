from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Jumun(BaseModel):
    jmno : int
    mno  :int
    prdno :int
    size  :int
    price:int
    qty :int
    postcode :int
    addr : str
    phone :int

    class Config:
        from_attributes = True


