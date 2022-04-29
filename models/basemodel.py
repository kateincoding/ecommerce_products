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

    def save(self):
        """save"""
        models.storage.new(self)
        models.storage.save()

    def delete(self):
        models.storage.delete(self)
