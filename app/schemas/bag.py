
from pydantic import BaseModel

class Bag(BaseModel):
    bno = int
    prdno = int
    jpname = str
    size = str
    price = int
    stack = int


    class Config:
        from_attributes = True


