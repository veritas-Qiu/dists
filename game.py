import pymysql
import sched
import time
from apscheduler.schedulers.background import BackgroundScheduler
import json
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

prices = {
    
    '钻石项链': 1680,
    '魔镜': 980,
    '玫瑰花': 20,
    '灯牌': 520,
    '荧光棒': 5
}

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
    total = {}
    # scheduler.add_job(sql_query, 'interval', args=[db, 'select acceptUserId, acceptUserName from live_3874066 group by acceptUserId'], seconds=60)
    req = sql_query(db, 'select acceptUserId, acceptUserName, presentName, presentNum from live_3874066 where liveid=850763643067633664')
    if req != None: 
        for line in req:
            if line[1] == None:
                continue
            if line[1] not in total:
                total[line[1]] = 0
            if line[2] not in prices:
                print(f'Unknown present: {line[2]}')
            else:
                total[line[1]] += prices[line[2]] * line[3]
    
    # print(total)
    total_show = sorted(total.items(), key=lambda x: x[1], reverse=False)
    names = [x[0] for x in total_show]
    values = [x[1] for x in total_show]
    
    norm = plt.Normalize(min(values), max(values))
    norm_values = norm(values)
    map_vir = plt.cm.get_cmap('jet')
    colors = map_vir(norm_values)
    
    plt.barh(names, values, color=colors)
    for i, v in enumerate(values):
        plt.text(v + 3, i - 0.25, str(v), color='blue', fontweight='bold')
    # plt.yticks(rotation=70)
    plt.show()
            
        

if __name__ == '__main__':
    main()
