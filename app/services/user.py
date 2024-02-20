from sqlalchemy import func, select

from app.dbfactory import Session
from app.models.member import Member, User


class UserService:
    # @staticmethod
    # def product_convert(pdto):
    #     data = pdto.model_dump()
    #     pb = Product(**data)
    #     data = {
    #         'prdname': pb.prdname,
    #         'category': pb.category,
    #         'stack': pb.stack,
    #         'price': pb.price,
    #         'contents': pb.contents
    #     }
    #
    #     return data

    @staticmethod
    def select_user():
        # stnum = (cpg - 1) * 10
        with Session() as sess:
            # cnt = sess.query(func.count(Member.mno)).scalar()
            stmt = select(Member.mno, Member.userid, Member.name, Member.email,
                          Member.addr, Member.birth, Member.phone, Member.point, Member.regdate, User.usertype) \
                .join_from(Member, User) \
                .order_by(Member.mno.desc()).offset(0).limit(25)
            result = sess.execute(stmt)

        return result

    # @staticmethod
    # def insert_product(pdto):
    #     data = ProductService.product_convert(pdto)
    #     with Session() as sess:
    #         stmt = insert(Product).values(data)
    #         result = sess.execute(stmt)
    #         sess.commit()
    #
    #     return result
