from app.models.member import Member
from sqlalchemy import insert, select, update
from app.dbfactory import Session

class MemberService:

    @staticmethod
    def member_convert(mdto):
        data = mdto.model_dump()
        mb = Member(**data)
        data = {
            'userid': mb.userid,
            'passwd': mb.passwd,
            'name': mb.name,
            'email': mb.email,
            'addr': mb.addr,
            'birth': mb.birth,
            'phone': mb.phone
        }

        return data

    @staticmethod
    def insert_member(mdto):
        data = MemberService.member_convert(mdto)

        with Session() as sess:
            stmt = insert(Member).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result

    @staticmethod
    def select_one(mno):
        with Session() as sess:
            stmt = select(Member).filter_by(mno=mno)
            result = sess.execute(stmt).first()

        return result

    @staticmethod
    def update_member(mdto, mno):
        data = MemberService.member_convert(mdto)

        with Session() as sess:
            stmt = update(Member).filter_by(mno=mno)\
                .values(name=data['name'], passwd=data['passwd'], email=data['email'], addr=data['addr'], birth=data['birth'], phone=data['phone'])
            result = sess.execute(stmt)
            sess.commit()

        return result