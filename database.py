from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_URL = 'mysql+pymysql://root@localhost/books'

engine = create_engine(SQLALCHEMY_URL)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()
