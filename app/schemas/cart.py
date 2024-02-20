from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Cart(BaseModel):
    cno = int
    jpno = int
    jpname = str
    size = str
    price = int
    stack = int


    class Config:
        from_attributes = True