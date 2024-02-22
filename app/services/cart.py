import os
from sqlalchemy import insert, select, delete
from app.models.jumun import Jumun
from sqlalchemy import func
from app.models.cart import Cart
from app.models.product import PrdAttach,Product
from app.dbfactory import Session
from sqlalchemy import select
from app.models.member import Member
from app.services.product import UPLOAD_DIR


class CartService:


    @staticmethod
    def insert_cart(prdno,mno):

        data = {'mno':mno, 'prdno': prdno, 'size':1, 'qty':1, 'price': 10000}

        with Session() as sess:
            stmt = insert(Cart).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result


    @staticmethod
    def select_cart(mno):
        with Session() as sess:
            stmt = select(Cart.cno,Cart.mno,Cart.prdno,Cart.size, Cart.qty,Cart.cno,
                          PrdAttach.img1,Product.prdname, Product.price)\
            .select_from(Cart).join(Product, Cart.prdno == Product.prdno)\
            .join(PrdAttach, PrdAttach.prdno == Product.prdno) \
            .where(Cart.mno == mno)
            result = sess.execute(stmt).fetchall()

        return result


    @staticmethod
    def selectone_cart(userid):


        with Session() as sess:
            result = sess.query(Cart).filter_by(userid=userid).scalar()
            return result

    @staticmethod
    def selectone_jumun(userid):


        with Session() as sess:
            result = sess.query(Jumun).filter_by(userid=userid).scalar()
            return result

    @staticmethod
    def select_jumun_cart(jmcno):
        with Session() as sess:
            stmt = select(Cart.cno,Cart.mno,Cart.prdno,Cart.size, Cart.qty,Cart.cno,
                      PrdAttach.img1,Product.prdname, Product.price) \
            .select_from(Cart).join(Product, Cart.prdno == Product.prdno) \
            .join(PrdAttach, PrdAttach.prdno == Product.prdno) \
            .where(Cart.cno == jmcno)
        result = sess.execute(stmt).fetchall()

        return result


    @staticmethod
    def select_jumun_user(jmmno):
        with Session() as sess:

            stmt = select(Member.mno,Member.userid,Member.name,Member.email, Member.addr,Member.phone,
                          Cart.cno, Cart.prdno) \
                .select_from(Member).join(Cart, Member.mno == Cart.mno) \
                .where(Member.mno == jmmno)
        result = sess.execute(stmt)

        return result

    @staticmethod
    def delete_cart(cno):
        with Session() as sess:

            stmt = delete(Cart).where(Cart.cno == cno)
            # 생성된 쿼리 실행
            result = sess.execute(stmt)
            # 변경 사항 커밋
            sess.commit()

        return result





