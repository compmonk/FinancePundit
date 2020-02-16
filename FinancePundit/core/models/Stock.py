from uuid import uuid4 as UUID

from mongoengine import Document
from mongoengine.fields import *


class Stock(Document):
    id = UUIDField(required=True, primary_key=True, default=UUID)
    symbol = StringField()
    name = StringField()
    market = StringField()
    sector = StringField()
    initial = DecimalField()
    volatility = FloatField()

    def __repr__(self):
        return "{0} ({1})".format(self.symbol, self.name[:30])

    def __str__(self):
        return "{0} ({1})".format(self.symbol, self.name[:30])
