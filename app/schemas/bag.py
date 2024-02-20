from datetime import datetime
from typing import Optional

from pydantic import BaseModel

class Bag(BaseModel):
    bno = int
    jpno = int
    jpname = str
    size = str
    price = int
    stack = int


    class Config:
        from_attributes = True


