import os
from sqlalchemy import insert, select
from app.models.jumun import Jumun, JumunAttach
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
    def insert_gallery(jmdto,fname,fsize):
        # 변환된 이미지 정보를 gallery 테이블에 저장
        data = JumunService.jumun_convert(jmdto)

        with Session() as sess:
            stmt = insert(Jumun).values(data)
            result = sess.execute(stmt)
            sess.commit()

            data = {'fname': fname, 'fsize': fsize,
                    'gno' : result.inserted_primary_key[0]}
            print(result.inserted_primary_key)
            stmt = insert(JumunAttach).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

    def select_jumun(jmdto):
        data = JumunService



