from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

# 1. open db connection
app = Flask(__name__)
app.config.from_pyfile('app.cfg')
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)

# class for data mapping
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    assword = Column(String)

    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

Base.metadata.create_all(engine)
# 2. insert one film
ed_user = User('ed', 'Ed Jones', 'edspassword')
Session = sessionmaker(bind=engine)
session = Session()
#session.add(ed_user)
#u1 = User(name='ed', fullname='Ed Jones', password='foobar')
#our_user = session.query(User).filter_by(name='ed').first()
session.commit()

# 3. get all films

# 4. insert all films into film table
# for film in films:
#     DBSession.add(Film(xxx='',))

# 5. create BFI table insert film FKs
# 6. create IMDB table insert film FKs
# 7. create oscar table insert film FKs
# 8. create table for ultimate movies, have function to drop and regenerate the list
