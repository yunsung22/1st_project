from app.models.product import Product
from sqlalchemy import insert

class AdminService:

    @staticmethod
    def member_convert(mdto):
        data = mdto.model_dump()
        mb = Product(**data)
        data = {
            'userid': mb.userid,
            'passwd': mb.passwd,
            'name': mb.name,
            'email': mb.email
        }

        return data

    @staticmethod
    def insert_member(mdto):
        data = AdminService.member_convert(mdto)
        from app.dbfactory import Session
        with Session() as sess:
            stmt = insert(Product).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result