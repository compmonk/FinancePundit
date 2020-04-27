from mongoengine import EmbeddedDocument
from mongoengine.fields import *

from .Stock import Stock


class StockVolume(EmbeddedDocument):
    stock = ReferenceField(Stock, required=True)
    volume = FloatField(default=0)

    def __str__(self):
        return "[{0}] - ({1})".format(self.stock.symbol, self.volume)

    def __repr__(self):
        return "[{0}] - ({1})".format(self.stock.symbol, self.volume)
