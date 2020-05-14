# This code works like a scheduler. This will send the curl request to heroku like we did from the command line.
# pip install apscheduler.
# This code should be added to Procfile: clock: python periodic_requests.py
import requests
import pytz
from apscheduler.schedulers.twisted import TwistedScheduler
from twisted.internet import reactor


def send_requests():
    requests.post("https://powerful-wildwood-97969.herokuapp.com/schedule.json", data={
        'project': 'default',
        'spider': 'coin_selenium'
    })


if __name__ == '__main__':
    scheduler = TwistedScheduler(timezone=pytz.utc)
    scheduler.add_job(send_requests, 'cron', day_of_week='mon-sun', hour='22', minute='50')

    scheduler.start()
    reactor.run()
    