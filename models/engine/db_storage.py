#!/usr/bin/env python3
"""Clase de base de datos"""
from os import getenv
from sqlalchemy import create_engine, Metadata
from models.category import Category
from models.product import Product
from logging import info

sql = 'mysql+mysqldb://{}:{}@{}:3306/{}'
user = getenv('DB_USER')
pssw = getenv('DB_PASSWORD')
host = getenv('DB_HOST')
db = getenv('DB_DATABASE')

class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine(sql.format(user, pssw, host, db),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """Queries of db"""
        if not cls:
            res_list = self.__session.query(Category)
            res_list = self.__session.query(Product)
        else:
            res_list = self.__session.query(cls)
        return ('{}.{}'format(type(obj).__name__, obj.id): obj
                for obj in res_list}

    def new(self, obj):
        """add a new object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current db session"""
        self.__session.commit()
