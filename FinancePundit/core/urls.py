from django.urls import path

from .views import StockList, StockDetail

urlpatterns = [
    path(r'stocks', StockList.as_view({'get': 'list'}), name='stock-list'),
    path(r'stocks/<uuid:id>', StockDetail.as_view(), name='stock-detail'),
]
