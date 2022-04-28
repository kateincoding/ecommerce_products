#!/usr/bin/python3
"""base class for all models in bsale"""
from models.basemodel import Basemodel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey


class Product(Basemodel, Base):
    """A base class for all bsale class"""
    __tablename__ = "product"
    url_image = Column(String(255), nullable=True)
    price = Column(Float, nullable=True)
    discount = Column(Integer(11), nullable=True)
    category = Column(Integer(11), ForeignKey('category.id'), nullable=True)
