# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import signal

import redis
import time

from scrapy.conf import settings

from .settings import *

from AMA_ANALYSIS.Identify_country import identify_Country
from AMA_ANALYSIS_TEST.show_respones_html import show_responses_html
from AMA_DATABASE.Remove_duplicate import remove_obj
from AMA_DATABASE.Xuggest_myredis import myredis_obj
from AMA_REQUEST.Construct_url import counstruct_Url
from multiprocessing import Process,Queue,Lock
from threading import Thread
##此导入不能删，使用了eval,
from AMA_ANALYSIS.use_analysis import using_analysis_obj
from AMA_REQUEST.repeat_handler import repeat_handle_obj
import  logging


class AmazonscrapyPipeline(object):

    def __init__(self):
        self.host = settings['REDIS_POST_HOST']['HOST']
        self.port = settings['REDIS_POST_HOST']['POST']
        self.pass_word = settings['pass_word']
        self.lock = Lock()

    def open_spider(self, spider):

        try:
            # self.host = settings['REDIS_POST_HOST']['HOST']
            # self.port = settings['REDIS_POST_HOST']['POST']

            self.host = settings['REDIS_HOST']
            self.port = settings['REDIS_PORT']
            # 创建redis链接池
            pool = redis.ConnectionPool(host=self.host, port=self.port)
            self.redis_obj = redis.Redis(connection_pool=pool)
            # 开启放入一个允许存入redis
            # # if not self.redis_obj.lpop('token'):
            #     self.redis_obj.rpush('token','token')
            # time.sleep(1)
            # # if not self.redis_obj.lpop('pid_code'):
            #     self.redis_obj.rpush('pid_code','pid_code')

            # 忽略子进程死亡发送的信号，处理僵尸进程
            signal.signal(signal.SIGCHLD, signal.SIG_IGN)
            # 开辟管道，用于传送pid号
            self.q = Queue()
        except Exception as e:
            logging.exception('open_spider')
        # 创建专门处理子进程的子进程
        # p = Process(target=self.handle_Child,args=(self.q,self.redis_obj))
        # p.daemon = True
        # p.start()
        return self.redis_obj

    # def kill_Child(self,Child_pid):
    #     '''定时杀死子进程'''
    #     time.sleep(40)
    #     try:
    #         os.kill(Child_pid,signal.SIGINT)
    #     except Exception as e:
    #         pass
    #
    # def handle_Child(self,q,redis_obj):
    #     '''
    #     专门获取所有的子进程pid，并分配线程去定时处理子进程
    #     :param q:
    #     :return:
    #     '''
    #     while True:
    #         # Child_pid = q.get()
    #
    #         Child_pid = redis_obj.blpop('pid_list')
    #         t =Thread(target=self.kill_Child,args=(Child_pid,))
    #         t.start()
    #         pass

    def Analysis(self,responses,url,spider,lock,q,redis_obj):
        '''
        每个子进程的处理逻辑
        :param responses:
        :param url:
        :param spider:
        :return:
        '''

        # signal.alarm(40)
        try:
            country = identify_Country(url)
            print(country)
            product_info = eval('using_analysis_obj.{}_analysis(all_response=responses,url=url)'.format(country))
            # print('product_info:',product_info)
            lock.acquire()
            if repeat_handle_obj.Check_OK(redsi_obj=redis_obj,product_info=product_info):

                # redis_obj.blpop('token',0)
                myredis_obj.submit_Product_info(redis_obj=redis_obj, product_info=product_info)
                # redis_obj.rpush('token', 'AMAZON_pass')
                print('product_info:', product_info)

            else:
                redis_obj.rpush(redis_start_url,url)
                logging.log(logging.WARNING,'重复处理：'+url)
            lock.release()
        except Exception as e:
            logging.exception('Analysis_Process')
        # print('product_info:', product_info)

        # f.close()

        ##将关联的ＡＳＩＮ构建函数后放入爬虫列表 和　保存下来

        # for ASIN in product_info['Link_ASIN']['Link_Size_ASIN_list']:
        #     url = counstruct_Url(country=product_info['Country'],ASIN=ASIN)
        #     if url:
        #         redis_obj.rpush('top_product_url',url)
        #         pass
        #
        # for ASIN in product_info['Link_ASIN']['Link_Color_ASIN_list']:
        #     url = counstruct_Url(country=product_info['Country'],ASIN=ASIN)
        #     if url:
        #         redis_obj.rpush('top_product_url',url)
                # pass

        # myredis_obj.add_Url(redis_obj=redis_obj,submit_key='top_product_url',Recommend_product_url_list=product_info['Recommend_product_url_list'])
        os._exit(0)
        return product_info



    def process_item(self, item, spider):

        responses = item['response'].text
        # show_responses_html(responses)
        print('responses OK')
        self.url = item['response'].url

        #使用线程
        try:
            t = Process(target=self.Analysis,args=(responses,self.url,spider,self.lock,self.q,self.redis_obj))
            # t = Thread(target=self.Analysis,args=(responses,self.url,spider,self.lock,self.q,self.redis_obj))
            t.start()
            pass
        except Exception as e:
            logging.exception('start_Process')
            print('err:',os.getpid())
            try:
                self.redis_obj.rpush('start_url',self.url)
            except Exception as e:
                pass
            os._exit(0)
        return item












