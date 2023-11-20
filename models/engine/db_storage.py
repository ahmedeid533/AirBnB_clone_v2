#!/usr/bin/python3
"""DB storage"""
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from models.base_model import Base
from models.user import User
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """new engine"""

    __engine = None
    __session = None

    def __init__(self):
        """start the engine"""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on db by class name or select * """
        if cls is None:
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            Q_result = self.__session.query(cls)
        return {"{}.{}".format(type(i).__name__, i.id): i for i in Q_result}
    
    def new(self, obj):
        """add new record"""
        self.__session.add(obj)
    
    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete record from DB"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
            get the DATA from DB to workplace
            scoped_session - to make sure your Session is thread-safe
        """
        Base.metadata.create_all(self.__engine)
        session_maker = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        get_Session = scoped_session(session_maker)
        self.__session = get_Session()

    def close(self):
        """hea end of work"""
        self.__session.close()

