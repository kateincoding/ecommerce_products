#!/usr/bin/python3
"""base class for all models in bsale"""
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Basemodel:
    """A base class for all bsale class"""
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(255), nullable=True)

    def __init__(self, *args, **kwargs):
        """Initiate a new model"""
        pass

    def __str__(self):
        """String representation of the Basemodel class"""
        print(self.__class__.__name__)
        print(self.id)
        print(self.__dict__)
        return "[{:s}] ({:d}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """save"""
        models.storage.new(self)
        models.storage.save()


    def to_dict(self, save_fs=None):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        return new_dict


    def delete(self):
        models.storage.delete(self)
