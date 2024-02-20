import os
from sqlalchemy import insert, select
from app.models.jumun import Jumun
from app.dbfactory import Session
from sqlalchemy import select
from app.services.product import UPLOAD_DIR


class JumunService:
    @staticmethod
    def jumun_convert(jmdto):
        data = jmdto.model_dump()
        jm = Jumun(**data)
        data = {'userloca' : jm.userloca,
                'stack':jm.stack,
                'price':jm.price,
                'email':jm.email,
                'name':jm.name,
                'postalcode':jm.postalcode,
                'phone':jm.phone}
        return data



    @staticmethod
    def insert_jumun(jmdto):

        data = JumunService.jumun_convert(jmdto)

        with Session() as sess:
            stmt = insert(Jumun).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result


    @staticmethod
    def select_jumun():
        with Session() as sess:
            stmt = select(Jumun.jmno, Jumun.userno, Jumun.jpno, Jumun.size,
                          Jumun.price, Jumun.stack, Jumun.postcode, Jumun.addr
                          , Jumun.phone) \
                .join_from(Jumun) \
                .order_by(Jumun.jmno.desc()).offset(0).limit(10)
            result = sess.execute(stmt)
            sess.commit()
            return result

    @staticmethod
    def insert_jumun(prdno, userid):
        pass






