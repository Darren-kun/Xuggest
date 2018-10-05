import signal

import time

from scrapy.conf import settings

import add_mypackage

from settings import *
import redis
from scrapy import cmdline
from multiprocessing import Process,Pool
from threading import Thread


# from Child_Amazonscrapy import run_child_scrapy


##为连接服务器处的 redis-server



spiders_list = [
                    ('ama_spiders',status_code),
                    #('ama_spiders_02',status_code_02),
                    ]


print('status_key',spiders_list)
url_key = 'immeditately'
host = settings['REDIS_POST_HOST']['HOST']
port = settings['REDIS_POST_HOST']['POST']
print('port:',port)
print('host:',host)
redis_obj = redis.Redis(host=host,port=port)

def run_AMAZONscrapy(spider_name):
    '''
    启动主爬虫
    :return:
    '''
    cmdline.execute("scrapy crawl {} ".format(spider_name).split())
    # cmdline.execute("scrapy crawl ama_spiders -s LOG_FILE=all.log".split())

# def run_child_Amazonscrapy(redis_obj,url,info_key='immeditately_info'):
#     '''
#     启动子爬虫
#     :return:
#     '''
#     immeditately_info = run_child_scrapy()
#     redis_obj.rpush(info_key,immeditately_info)
#     print('immeditately_info:',immeditately_info)
#     return immeditately_info

# def immeditately():
#     while True:
#         url = redis_obj.blpop(url_key, 0)[1].decode('utf8')
#         t = Thread(target=run_child_Amazonscrapy,args=(redis_obj,url))
#         t.start()
#     pass
#

def get_Status(name_status):
    '''
    监控爬虫，在ｒｅｄｉｓ　里获取　ｓｔａｔｕｓ
    :return:
    '''
    spider_name = name_status[0]
    status_key = name_status[1]
    while True:
        status = redis_obj.get(status_key)
        if status:
            print('运行中')
            pass
        else:
            print ('重启爬虫')
            p = Process(target=run_AMAZONscrapy,args=(spider_name,))
            p.start()
            p.join()
        time.sleep(3)


def run():
    '''
    启动监控程序
    :return:
    '''

    for name_status in spiders_list:
        t = Thread(target=get_Status,args=(name_status,))
        t.start()
    redis_obj.rpush('token','token')



if __name__ == "__main__":
    run()

# cmdline.execute("scrapy crawl ama_spiders -s LOG_FILE=all.log".split())

# cmdline.execute("scrapy crawl ama_spiders ".split())
