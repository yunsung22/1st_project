import os

from app.models.product import Product, PrdAttach
from sqlalchemy import insert, select, update, func, delete, and_
from app.dbfactory import Session

UPLOAD_DIR = r'C:\Java\nginx-1.25.3\html\cdn'


class ProductService:
    @staticmethod
    def product_convert(pdto):
        data = pdto.model_dump()
        pb = Product(**data)
        data = {
            'prdname': pb.prdname,
            'category': pb.category,
            'stack': pb.stack,
            'price': pb.price,
            'contents': pb.contents
        }

        return data

    @staticmethod
    def prdattach_convert(padto):
        data = padto.model_dump()
        pab = PrdAttach(**data)
        data = {
            'prdno': pab.prdno,
            'img1': pab.img1,
            'img2': pab.img2,
            'img3': pab.img3,
            'img4': pab.img4
        }

        return data

    @staticmethod
    def insert_product(pdto):
        data = ProductService.product_convert(pdto)
        with Session() as sess:
            stmt = insert(Product).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def insert_prdattach(padto):
        data = ProductService.prdattach_convert(padto)
        with Session() as sess:
            stmt = insert(PrdAttach).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def select_product(cpg):
        stnum = (cpg - 1) * 10
        with Session() as sess:
            cnt = sess.query(func.count(Product.prdno)).scalar()
            stmt = select(Product.prdno, Product.prdname, Product.category, Product.stack,
                          Product.price, Product.salepoint, PrdAttach.img1)\
            .join_from(Product, PrdAttach) \
            .order_by(Product.prdno.desc()).offset(stnum).limit(10)
            result = sess.execute(stmt)

        return result, cnt


    @staticmethod
    def selectone_product(prdno):
        with Session() as sess:
            stmt = select(Product, PrdAttach).join_from(Product,PrdAttach).filter_by(prdno=prdno)
            result = sess.execute(stmt).first()
            return result


    @staticmethod
    def find_select_product(category, search, cpg):
        stnum = (cpg - 1) * 10
        with Session() as sess:
            stmt = select(Product.prdno, Product.prdname, Product.category, Product.stack,
                          Product.price, Product.salepoint, PrdAttach.img1).join_from(Product,PrdAttach)

            myfilter = and_(Product.prdname.like(search), Product.category.like(category))
            if search == '' and category != '':  myfilter = Product.category.like(category)
            elif search != '' and category == '': myfilter = Product.prdname.like(search)

            stmt = stmt.filter(myfilter) \
                .order_by(Product.prdno.desc()).offset(stnum).limit(10)
            result = sess.execute(stmt)

            cnt = sess.query(func.count(Product.prdno)).filter(myfilter).scalar() # 총 게시글 수

        return result, cnt


    @staticmethod
    async def process_upload(images):
        list = []
        for image in images:
            nfname = image.filename
            fname = os.path.join(UPLOAD_DIR, nfname)
            list.append(nfname)
            content = await image.read()
            with open(fname, 'wb') as f:
                f.write(content)

        return list


    @staticmethod
    def update_product(rows_data):
        with Session() as sess:
            for row_data in rows_data.values():
                print(row_data.salepoint, row_data.prdno)
                stmt = update(Product).where(Product.prdno == row_data.prdno) \
                    .values(prdname=row_data.prdname, stack=row_data.stack, price=row_data.price, salepoint=row_data.salepoint)
                result = sess.execute(stmt)
                sess.commit()

        return result

    @staticmethod
    def delete_product(del_data):
        prdnos = list(del_data.values())[0]
        print(prdnos)
        with Session() as sess:
            for prdno in prdnos:
                stmt = delete(Product).where(Product.prdno == prdno)
                sess.execute(stmt)
                stmt2 = delete(PrdAttach).where(PrdAttach.prdno == prdno)
                result = sess.execute(stmt2)
                sess.commit()
        return result

