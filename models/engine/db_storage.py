#!/usr/bin/python3
import models
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """Database storage class
    Attributes: __engine, __session
    """
    __engine = None
    __session = None

    def __init__(self):
        """Creates the engine"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()

    def all(self, cls=None):
        """Method that queries on the currect database session"""
        objects_dictionary = {}
        classes = [State, City, User, Place, Review, Amenity]
        if cls:
            classes = [cls]
        for j in classes:
            for k in self.__session.query(j).all():
                key = "{}.{}".format(type(k).__name__, k.id)
                objects_dictionary[key] = k
        return objects_dictionary

    def new(self, obj):
        """Method that adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Method that commits all changes of the current database session"""

        self.__session.commit()

    def delete(self, obj=None):
        """Method that deletes from the current database
        session obj if not None"""

        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Method that creates all tables in the database"""

        Base.metadata.create_all(self.__engine)
        my_session = sessionmaker(bind=self.__engine,
                                  expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()
