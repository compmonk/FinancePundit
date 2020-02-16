from rest_framework.serializers import UUIDField
from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer

from ..models.Stock import Stock
from ..models.StockVolume import StockVolume
from ..serializers.StockSerializer import StockSerializer


class StockVolumeSerializer(EmbeddedDocumentSerializer):
    stock = StockSerializer

    class Meta:
        model = StockVolume
        fields = '__all__'
        depth = 2
    #
    # def create(self, validated_data):
    #     stock = Stock.objects(id=validated_data.pop('stockId')).get()
    #     stock_volume = super(StockVolumeSerializer, self).create(validated_data)
    #     stock_volume.stock = stock
    #     stock_volume.save()
    #     return stock_volume
