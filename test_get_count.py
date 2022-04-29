#!/usr/bin/python3
from models import storage
from models.category import Category
from models.product import Product

print("All objects: {}".format(storage.count()))
print("Category objects: {}".format(storage.count(Category)))
print("Product objects: {}".format(storage.count(Product)))
