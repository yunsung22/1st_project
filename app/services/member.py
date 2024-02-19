from app.models.member import Member
from sqlalchemy import insert, select, update
from app.dbfactory import Session
import hashlib

class MemberService:

    @staticmethod
    def sha256_hash(passwd):
        """
        SHA-256 암호화 함수
        """
        hash_object = hashlib.sha256()
        hash_object.update(passwd.encode('utf-8'))
        return hash_object.hexdigest()

    @staticmethod
    def member_convert(mdto):
        data = mdto.model_dump()
        mb = Member(**data)
        data = {
            'userid': mb.userid,
            'passwd': MemberService.sha256_hash(mb.passwd),
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

    @staticmethod
    def check_login(userid, passwd):

        with Session() as sess:
            result = sess.query(Member).filter_by(userid=userid).scalar()

            if result and result.passwd == MemberService.sha256_hash(passwd):
                return result
            else:
                return None

    @staticmethod
    def select_one_member(userid):

        with Session() as sess:
            result = sess.query(Member).filter_by(userid=userid).scalar()
            return result