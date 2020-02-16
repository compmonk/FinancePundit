from uuid import uuid4 as UUID

from mongoengine.fields import *

from mongoengine import Document
from mongoengine.queryset import QuerySet, Q

from core.models.StockVolume import StockVolume

from core.models.Stock import Stock


class UserManager(QuerySet):

    def get_queryset(self):
        return self.all()

    def create_user(self, **data):
        user = {'firebaseId': data.get('localId', None)}
        user = self.create(**user)
        user.save()
        return user

    def update(self, upsert=False, multi=True, write_concern=None, full_result=False, **update):
        user = self.get(id=update.pop('id'))
        for stockVolume in update.pop('stockVolumes'):
            user.stockVolumes.append(StockVolume(
                stock=Stock.objects.get(id=stockVolume['stock']['id']),
                volume=stockVolume['volume']
            ))
        user.save()
        return user


class User(Document):
    id = UUIDField(required=True, primary_key=True, default=UUID)
    firebaseId = StringField(required=True)
    stockVolumes = EmbeddedDocumentListField(StockVolume)

    meta = {'queryset_class': UserManager}
