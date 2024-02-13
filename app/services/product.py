from app.models.product import Product
from sqlalchemy import insert, select
from app.dbfactory import Session

class ProductService:

    @staticmethod
    def product_convert(pdto):
        data = pdto.model_dump()
        pb = Product(**data)
        data = {
            'prdname': pb.prdname,
            'category': pb.category,
            'img' : pb.img,
            'stack': pb.stack,
            'price': pb.price
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
    def select_product():
        with Session() as sess:
            stmt = select(Product.prdno, Product.prdname, Product.category , Product.img , Product.stack,
                          Product.price, Product.salepoint)
            result = sess.execute(stmt).all()
            sess.commit()

        return result
