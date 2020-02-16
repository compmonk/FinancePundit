from rest_framework_mongoengine.serializers import DocumentSerializer

from ..models.Stock import Stock


class StockSerializer(DocumentSerializer):
    class Meta:
        model = Stock
        fields = [
            'id',
            'symbol',
            'name',
            'market',
            'sector'
        ]
