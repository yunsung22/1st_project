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

        # 비밀번호 암호화
        data['passwd'] = MemberService.sha256_hash(data['passwd'])

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

        print('new_passwd', data['passwd'])

        # 비밀번호 암호화
        new_passwd = None
        if data['passwd']:
            new_passwd = MemberService.sha256_hash(data['passwd'])

        with Session() as sess:
            stmt = update(Member).filter_by(mno=mno)

            # 비밀번호가 비어있지 않으면 업데이트 항목에 추가
            if new_passwd:
                stmt = stmt.values(name=data['name'], passwd=new_passwd, email=data['email'], addr=data['addr'], birth=data['birth'], phone=data['phone'])
            else:
                stmt = stmt.values(name=data['name'], email=data['email'], addr=data['addr'], birth=data['birth'], phone=data['phone'])

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