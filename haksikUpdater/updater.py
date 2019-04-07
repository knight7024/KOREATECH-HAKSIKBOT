from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.schedulers.blocking import BlockingScheduler
from .haksikApi import update_haksik

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_haksik, 'cron', hour=0)
    # scheduler.add_job(update_haksik, 'interval', minutes=1)
    scheduler.start()