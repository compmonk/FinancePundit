from rest_framework_mongoengine.serializers import DocumentSerializer
from rest_framework.fields import *

from ..models.Stock import Stock


class StockSerializer(DocumentSerializer):
    initial = DecimalField(read_only=True, decimal_places=2, max_digits=None)
    volatility = DecimalField(read_only=True, decimal_places=2, max_digits=None)

    class Meta:
        model = Stock
        fields = '__all__'
