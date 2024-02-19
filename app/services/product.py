import os

from app.models.product import Product, PrdAttach
from sqlalchemy import insert, select, update
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
            'price': pb.price
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
    def select_product():
        with Session() as sess:
            stmt = select(Product.prdno, Product.prdname, Product.category, Product.stack,
                          Product.price, Product.salepoint, PrdAttach.img1)\
            .join_from(Product, PrdAttach) \
            .order_by(Product.prdno.desc()).offset(0).limit(10)
            result = sess.execute(stmt)
            sess.commit()

        return result

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
        with (Session() as sess):
            for row_data in rows_data.values():
                print(row_data.salepoint, row_data.prdno)
                stmt = update(Product).where(Product.prdno == row_data.prdno) \
                    .values(prdname=row_data.prdname, stack=row_data.stack, price=row_data.price, salepoint=row_data.salepoint)
                result = sess.execute(stmt)
                sess.commit()

        return result
