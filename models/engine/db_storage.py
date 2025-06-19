#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base

class DBStorage:
    __engine = None
    __session = None
    classes = {"User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')
        conn = f"mysql+mysqldb://{user}:{password}@{host}/{database}"
        self.__engine = create_engine(conn, pool_pre_ping=True)
        ht = getenv('HBNB_ENV')
        if ht == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        obj_dict = {}
        if cls:
            if isinstance(cls, str):
                cls_obj = type(self).classes.get(cls)
            else:
                cls_obj = cls
            # If we still can't find it, return empty
            if cls_obj is None:
                return obj_dict
            # Query the class
            objs = self.__session.query(cls_obj).all()
            for obj in objs:
                key = f"{type(obj).__name__}.{obj.id}"
                obj_dict[key] = obj
        else:
            for ctyp in self.classes.values():
                objs = self.__session.query(ctyp).all()
                for obj in objs:
                    key = f"{type(obj).__name__}.{obj.id}"
                    obj_dict[key] = obj
        return obj_dict
    
    def new(self, obj):
        self.__session.add(obj)
    def save(self):
        self.__session.commit()
    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)
    def reload(self):
        from models.city import City
        from models.state import State
        Base.metadata.create_all(self.__engine)
        #Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))
        self.__session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        self.__session.remove()
