import schedule
import time
import threading

from .influx import InfluxClient, post_stock_volumes
from accounts.models.User import User


def scheduler():
    users = User.objects()
    influx_connection = InfluxClient()
    schedule.every(5).seconds.do(post_stock_volumes, influx_connection=influx_connection, users=users)

    while True:
        schedule.run_pending()
        time.sleep(2)
    pass


threading.Thread(target=scheduler).start()
