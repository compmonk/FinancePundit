import random

from influxdb import InfluxDBClient

from django.utils.timezone import now
from django.conf import settings


class InfluxPayload:
    def __init__(self, user, stock_volume):
        self.measurement = "stock"
        self.tags = {
            "name": stock_volume.stock.name,
            "market": stock_volume.stock.market,
            "symbol": stock_volume.stock.symbol,
            "sector": stock_volume.stock.sector,
            "user": user.firebaseId
        }
        self.time = now()
        self.fields = {
            "symbol": stock_volume.stock.symbol,
            "name": stock_volume.stock.name,
            "market": stock_volume.stock.market,
            "sector": stock_volume.stock.sector,
            "volume": stock_volume.volume,
            "value": round(float(stock_volume.stock.initial) * 2 * random.random(), 2),
            "user": user.firebaseId,
            "target": round(float(user.target) * 2 * random.random(), 2),
        }


class InfluxClient:
    def __init__(self):
        self.client = InfluxDBClient(host=settings.INFLUX_HOST,
                                     port=8086,
                                     username=settings.INFLUX_USER,
                                     password=settings.INFLUX_PASS,
                                     database=settings.INFLUX_DATABASE
                                     )


def post_stock_volumes(influx_connection, users):
    payload = []
    for user in users:
        for stock_volume in user.stockVolumes:
            payload.append(InfluxPayload(user, stock_volume).__dict__)

    if influx_connection.client.write_points(payload):
        print({
            "time": now().strftime("%Y%m%d%H%M%S"),
            "operation": "write",
            "success": True
        })
    else:
        print({
            "time": now().strftime("%Y%m%d%H%M%S"),
            "operation": "write",
            "success": True,
        })
