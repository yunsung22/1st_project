import os
from sqlalchemy import insert, select
from app.models.jumun import Jumun
from sqlalchemy import func
from app.models.cart import Cart
from app.dbfactory import Session
from sqlalchemy import select
from app.services.product import UPLOAD_DIR


class CartService:


    @staticmethod
    def insert_cart(cdto):

        data = {''}

        with Session() as sess:
            stmt = insert(Cart).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def select_card(cpg):
        stnum=(cpg-1)*10

        with (Session() as sess):


            cnt= sess.query(func.count(Cart.bno)).scalar()

            stmt = select(Cart.cno,Cart.jpno,Cart.jpname,
                          Cart.size,Cart.price,Cart.stack)\
                .order_by(Cart.bno.desc()).offset(stnum).limit(25)
            result = sess.execute(stmt)

        return result, cnt

    @staticmethod
    def selectone_cart(cno):

        with (Session() as sess):

            stmt = select(Cart).filter_by(cno=cno)
            result = sess.execute(stmt).first()
        return result
