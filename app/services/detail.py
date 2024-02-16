import os
from datetime import datetime

from app.dbfactory import Session
from sqlalchemy import insert, select, update, func, or_

from app.models.product import Product, GalAttach

# 이미지 파일 저장 경로 설정
UPLOAD_DIR = r'C:\Java\nginx-1.25.3\html\cdn'


class DetailService():
    @staticmethod
    def detail_convert(gdto):
        data = gdto.model_dump()
        # data.pop('response') # captcha 확인용 변수 response 제거
        gal = Product(**data)
        data = {'prdname':gal.prdname, 'price':gal.price, 'contents':gal.contents, 'stack':gal.stack, 'salepoint':gal.salepoint}
        return data

    @staticmethod
    def insert_detail(gdto, fname, fsize):
        data = DetailService.detail_convert(gdto)
        with Session() as sess:
            stmt = insert(Product).values(data)
            result = sess.execute(stmt)
            sess.commit()

            data = {'fname':fname, 'fsize':fsize,'prdno':result.inserted_primary_key[0]}
            stmt = insert(GalAttach).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    async def process_upload(attach):
        today = datetime.today().strftime('%Y%m%d%H%M%S')
        nfname = f'{today}{attach.filename}'
        fsize = attach.size
        # os.path.join(A,B) => A/B (경로 생성)
        fname = os.path.join(UPLOAD_DIR, nfname)

        # 비동기 처리를 위해 함수에 await 지시자 추가
        # 이럴 경우 함수 정의 부분에 async라는 지시자 추가 필요
        content = await attach.read() #업로드한 파일의 내용을 비동기로 모두 읽어옴

        with open(fname, 'wb') as f:
            f.write(content)

        return nfname, fsize


    @staticmethod
    def select_detail(cpg):
        stnum = (cpg - 1 ) * 25
        with (Session() as sess):
            cnt = sess.query(func.count(Product.prdno)).scalar() # 총 게시글 수
            stmt = select(Product.prdno, Product.prdname, Product.price, GalAttach.fname)\
            .join_from(Product, GalAttach)\
            .order_by(Product.prdno.desc())\
            .offset(stnum).limit(25)
            result = sess.execute(stmt)

        return result, cnt


    @staticmethod
    def selectone_detail(prdno):
        with Session() as sess:
            stmt = select(Product, GalAttach).join_from(Product,GalAttach).filter_by(prdno=prdno)
            result = sess.execute(stmt).first()
            return result
