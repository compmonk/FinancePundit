from mongoengine import EmbeddedDocument
from mongoengine.fields import *

from .Stock import Stock


class StockVolume(EmbeddedDocument):
    stock = ReferenceField(Stock, required=True)
    volume = FloatField(default=0)
