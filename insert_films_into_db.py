from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from models.sa_film import get_film_class
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. open db connection
app = Flask(__name__)
app.config.from_pyfile('app.cfg')
db = SQLAlchemy(app)

#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
db_session = sessionmaker(bind=engine)

# 2. insert one film
Base = declarative_base()
Film = get_film_class(Base)
db_session.add(Film(name='blah', year='1942'))
db_session.flush()
# 3. get all films

# 4. insert all films into film table
# for film in films:
#     DBSession.add(Film(xxx='',))

# 5. create BFI table insert film FKs
# 6. create IMDB table insert film FKs
# 7. create oscar table insert film FKs
# 8. create table for ultimate movies, have function to drop and regenerate the list
