from random import randrange

from influxdb import InfluxDBClient

from django.utils.timezone import now
from django.conf import settings


class InfluxPayload:
    def __init__(self, stock_volume):
        # self.time = now()
        # self.symbol = stock_volume.stock.symbol
        # self.name = stock_volume.stock.name
        # self.market = stock_volume.stock.market
        # self.volume = stock_volume.volume
        # self.value = randrange(stock_volume.stock.initial * (1 - stock_volume.stock.volatility),
        #                        stock_volume.stock.initial * (1 + stock_volume.stock.volatility))

        self.measurement = stock_volume.stock.name
        self.tags = {
            "name": stock_volume.stock.name,
            "market": stock_volume.stock.market,
            "symbol": stock_volume.stock.symbol,
            "sector": stock_volume.stock.sector,

        }
        self.time = now()
        self.fields = {
            "symbol": stock_volume.stock.symbol,
            "name": stock_volume.stock.name,
            "market": stock_volume.stock.market,
            "sector": stock_volume.stock.sector,
            "volume": stock_volume.volume,
            "value": randrange(stock_volume.stock.initial * (1 - stock_volume.stock.volatility),
                               stock_volume.stock.initial * (1 + stock_volume.stock.volatility))
        }


class InfluxService:
    def __init__(self):
        self.client = InfluxDBClient(settings.INFLUX_HOST,
                                     443,
                                     settings.INFLUX_USER,
                                     settings.INFLUX_PASS,
                                     settings.INFLUX_DATABASE,
                                     True,
                                     False)

    def post_stock_volume(self, stock_volume):
        payload = InfluxPayload(stock_volume).__dict__
        if self.client.write(payload):
            print({
                "time": now(),
                "operation": "write",
                "success": True,
                "payload": payload
            })
        else:
            print({
                "time": now(),
                "operation": "write",
                "success": True,
                "payload": payload
            })
