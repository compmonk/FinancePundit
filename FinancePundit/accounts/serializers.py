from rest_framework_mongoengine.serializers import DocumentSerializer

from .models.User import User
from core.serializers.StockVolumeSerializer import StockVolumeSerializer


class UserSerializer(DocumentSerializer):
    stockVolumes = StockVolumeSerializer(many=True)

    class Meta:
        model = User
        fields = '__all__'
