from sqlalchemy import func, select, update, delete

from app.dbfactory import Session
from app.models.member import Member, User


class UserService:
    @staticmethod
    def select_user(cpg):
        stnum = (cpg - 1) * 15
        with Session() as sess:
            cnt = sess.query(func.count(Member.mno)).scalar()
            stmt = select(Member.mno, Member.userid, Member.name, Member.email,
                          Member.addr, Member.birth, Member.phone, Member.point, Member.regdate, User.usertype) \
                .join_from(Member, User) \
                .order_by(Member.mno.desc()).offset(stnum).limit(15)
            result = sess.execute(stmt)

        return result, cnt

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


    @staticmethod
    def search_select_user(ftype, fkey, cpg):
        stnum = (cpg - 1) * 15
        with Session() as sess:
            stmt = select(Member.mno, Member.userid, Member.name, Member.email, Member.addr, Member.birth, Member.phone, Member.point, Member.regdate, User.usertype) \
                          .join_from(Member, User)

            myfilter = Member.mno.like(fkey)
            if ftype == 'nickname': myfilter = Member.userid.like(fkey)
            elif ftype == 'name': myfilter = Member.name.like(fkey)
            elif ftype == 'usertype':
                myfilter = User.usertype.like(fkey)
                cnt = sess.query(func.count(User.mno)).filter(myfilter).scalar()
                stmt = stmt.filter(myfilter).order_by(Member.mno.desc()).offset(stnum).limit(15)
                result = sess.execute(stmt)
                return result, cnt
            elif ftype == 'email': myfilter = Member.email.like(fkey)
            elif ftype == 'address': myfilter = Member.addr.like(fkey)
            elif ftype == 'birth': myfilter = Member.birth.like(fkey)
            elif ftype == 'phone': myfilter = Member.phone.like(fkey)

            stmt = stmt.filter(myfilter).order_by(Member.mno.desc()).offset(stnum).limit(15)
            result = sess.execute(stmt)
            cnt = sess.query(func.count(Member.mno)).filter(myfilter).scalar()

        return result, cnt
