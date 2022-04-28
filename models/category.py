#!/usr/bin/python3
"""base class for all models in bsale"""
from models.basemodel import Basemodel, Base
from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship, backref


class Category(Basemodel, Base):
    """A base class for all bsale class"""
    __tablename__ = 'category'
    product = relationship('Product', backref='category')
