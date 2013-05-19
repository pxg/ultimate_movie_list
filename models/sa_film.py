import datetime
from sqlalchemy import Column, Integer, String, DateTime


#TODO: do we need to wrap the class in the function?
def get_film_class(declarative_base):
    """
    Factory function to create an SQLAlchemy User model with a declarative
    base (for example db.Model from the Flask-SQLAlchemy extension).
    """
    class Film(declarative_base):
        """
        Implementation of User for SQLAlchemy.
        """
        # does the below line break flask?
        __tablename__ = 'film'
        id = Column(Integer, primary_key=True)
        name = Column(String(80), unique=True, nullable=False)
        director = Column(String(80), unique=True, nullable=True)  # TODO: move to it's own table
        year = Column(String(120), nullable=True)  # TODO: change type
        created = Column(DateTime(), default=datetime.datetime.utcnow)
        modified = Column(DateTime())  # can we autoset this?
    return Film
