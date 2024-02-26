from sqlalchemy import insert
from app.models.jumun import Jumun
from app.dbfactory import Session
from sqlalchemy import select
from app.models.product import Product
from app.models.product import PrdAttach


class JumunService:
    @staticmethod
    def jumun_convert(jmdto):
        data = jmdto.model_dump()
        data.pop('cno')
        jm = Jumun(**data)
        data = {'mno': jm.mno,
                'prdno': jm.prdno,
                'size' : 'Free',
                'addr' : jm.addr,
                'qty':jm.qty,
                'price':jm.price,
                'postcode':jm.postcode,
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
    def select_orderhistory(mno):
        with Session() as sess:

            stmt = select(Jumun.jmno,Jumun.mno,Jumun.prdno,Jumun.size, Jumun.qty,Jumun.price,
                          Jumun.postcode,Jumun.addr, Jumun.phone,Product.prdno,Product.prdname, PrdAttach.img1) \
                .select_from(Jumun).join(Product, Jumun.prdno == Product.prdno) \
                .join(PrdAttach, PrdAttach.prdno == Product.prdno) \
                .where(Jumun.mno == mno)
            result = sess.execute(stmt).fetchall()

        return result








