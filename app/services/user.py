from sqlalchemy import func, select, update, delete

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

    @staticmethod
    def update_user(acdto):
        with Session() as sess:
            stmt = update(User).where(User.mno == int(acdto['mno'])) \
                .values(usertype=acdto['usertype'])
            result = sess.execute(stmt)
            sess.commit()

        return result


    @staticmethod
    def delete_user(dudto):
        with Session() as sess:
            for mno in dudto['mno']:
                stmt = delete(Member).where(Member.mno == mno)
                sess.execute(stmt)
                stmt2 = delete(User).where(User.mno == mno)
                result = sess.execute(stmt2)
                sess.commit()
        return result
