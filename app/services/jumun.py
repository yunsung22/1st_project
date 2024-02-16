from sqlalchemy import insert

from app.models.member import Member
from app.dbfactory import Session

class JumunService():
    @staticmethod
    def jumun_convert(mdto):
        data = mdto.model_dump()
        mb = Member(**data)
        data = {'userid':mb.userid, 'passwd':mb.passwd, 'name':mb.name, 'email':mb.email}
        return data

    @staticmethod
    def insert_jumun(mdto):
        data = JumunService.jumun_convert(mdto)
        with Session() as sess:
            stmt = insert(Member).values(data)
            result = sess.execute(stmt)
            sess.commit()

        return result






