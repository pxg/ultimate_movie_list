from flask import Flask
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

# Show create table SQL
#Base.metadata.create_all(engine)
# 2. insert one film
edd_user = User('Fred', 'Fred Jones', 'eddspassword')
Session = sessionmaker(bind=engine)
session = Session()
session.add(edd_user)
session.commit()
