from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import config
from app.models import member, product, board, jumun, bag

engine = create_engine(config.db_conn, echo=True, connect_args={'check_same_thread':False})
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def db_startup():
    member.Base.metadata.create_all(engine)
    product.Base.metadata.create_all(engine)
    board.Base.metadata.create_all(engine)
    jumun.Base.metadata.create_all(engine)
    bag.Base.metadata.create_all(engine)
