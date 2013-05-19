from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.sa_film import get_film_class

# 1. open db connection
app = Flask(__name__)
app.config.from_pyfile('app.cfg')
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'], echo=True)
db = SQLAlchemy(app)

Film = get_film_class(db.Model)
film = Film(name='blah blah', year='1938', director='asdf')
Session = sessionmaker(bind=engine)
session = Session()
session.commit()

# 3. get all films

# 4. insert all films into film table
# for film in films:
#     DBSession.add(Film(xxx='',))

# 5. create BFI table insert film FKs
# 6. create IMDB table insert film FKs
# 7. create oscar table insert film FKs
# 8. create table for ultimate movies, have function to drop and regenerate the list
