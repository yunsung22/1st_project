import os
from sqlalchemy import insert, select
from app.models.jumun import Jumun
from app.models.cart import Cart
from app.dbfactory import Session
from sqlalchemy import select
from app.services.product import UPLOAD_DIR


class CartService:

    @staticmethod
    def cart_convert(cdto):
        # 클라이언트에서 전달받은 데이터를 dict형으로 변환
        data = cdto.model_dump()
        c = Cart(**data)
        data = {'jpname': c.jpname, 'size': c.size, 'price': c.price, 'stack': c.stack}
        return data

    @staticmethod
    def insert_cart(cdto):

        data = CartService.cart_convert(cdto)

        with Session() as sess:
            stmt = insert(Cart).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def selectone_cart(jpname):
        with Session() as sess:
            result = sess.query(Cart).filter_by(jpname=jpname).scalar()
            return result







