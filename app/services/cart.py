import os
from sqlalchemy import insert, select
from app.models.jumun import Jumun
from sqlalchemy import func
from app.models.cart import Cart
from app.models.product import PrdAttach,Product
from app.dbfactory import Session
from sqlalchemy import select
from app.services.product import UPLOAD_DIR


class CartService:


    @staticmethod
    def insert_cart(prdno,mno):

        data = {'mno':mno, 'jpno': prdno, 'size':1, 'qty':1, 'price': 10000}

        with Session() as sess:
            stmt = insert(Cart).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def select_cart():
        with Session() as sess:

            stmt = select(Cart.cno,Cart.mno,Cart.prdno,Cart.size
                          ,Cart.qty,Cart.cno,PrdAttach.img1,Product.prdname)\
            .join_from(Product,PrdAttach) \
            .order_by(Cart.cno.desc()).offset().limit(25)
            result = sess.execute(stmt).first()

        return result

    @staticmethod
    def selectone_cart(userid):


        with Session() as sess:
            result = sess.query(Cart).filter_by(userid=userid).scalar()
            return result


