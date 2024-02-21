from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Cart(BaseModel):
    cno = int
    mno = int
    prdno = int
    size = str
    qty = int
    price = int


    class Config:
        from_attributes = True