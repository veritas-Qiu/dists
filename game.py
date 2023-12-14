import pymysql
import sched
import time
from apscheduler.schedulers.background import BackgroundScheduler
import json

def sql_query(db:pymysql.Connection, query):
    cur = db.cursor()
    status = cur.execute(query)
    if status != 0:
        return cur.fetchall()
    else:
        return None
    
def main():
    db = pymysql.connect(host='42.192.118.224',
                         port=3306,
                         user='pocket48new',
                         password='pocket48new',
                         database='pocket48')
    scheduler = BackgroundScheduler()
    scheduler.add_job(sql_query, 'interval', args=[db, 'select * from user'], seconds=60)
