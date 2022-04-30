#!/usr/bin/env python3
"""Clase de base de datos"""
import models
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from models.basemodel import Basemodel, Base
from models.category import Category
from models.product import Product
from logging import info
# import pymysql

# pymysql.install_as_MySQLdb()

# sql = 'mysql+mysqldb://{}:{}@{}/{}'
# user = getenv('DB_USER')
# pssw = getenv('DB_PASSWORD')
# host = getenv('DB_HOST')
# db = getenv('DB_DATABASE')

classes = {"Category": Category, "Product": Product}

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        """instance of dbstorage"""
        user = getenv('DB_USER')
        pssw = getenv('DB_PASSWORD')
        host = getenv('DB_HOST')
        db = getenv('DB_DATABASE')
        sql = 'mysql+mysqldb://{}:{}@{}/{}'.format(user, pssw, host, db)
        print(sql)
        self.__engine = create_engine(sql, pool_pre_ping=True)

    def all(self, cls=None):
        """Queries of db"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current db session"""
        self.__session.commit()

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session"""
        self.__session.remove()


    def get(self, cls, id):
        """
        Returns the object based on the class name and
        its ID, or None if not found
        """
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (str(value.id) == str(id)):
                return value
        return None


    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()
        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())
        return count
