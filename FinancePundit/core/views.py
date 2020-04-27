from django.shortcuts import render, redirect
from rest_framework_mongoengine import viewsets
from rest_framework_mongoengine.generics import RetrieveUpdateDestroyAPIView

from .models.Stock import Stock
from .serializers.StockSerializer import StockSerializer


class StockList(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    def post(self, request):
        return self.create(request)


class StockDetail(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = StockSerializer
    queryset = Stock.objects

    def get(self, request, *args, **kwargs):
        return self.retrieve(self, request, *args, **kwargs)

    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def patch(self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(self, request, *args, **kwargs)


def dashboard(request):
    if request.session.get('userId', None) is not None:
        return render(request, "dashboard.html")
    else:
        return redirect("/")
