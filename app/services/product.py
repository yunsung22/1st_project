from app.models.product import Product
from sqlalchemy import insert
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