# -*- coding: utf-8 -*-
import os
import random
import scrapy
import time
from AMAZONscrapy.items import AmazonscrapyItem
from AMAZONscrapy.pipelines import AmazonscrapyPipeline
from scrapy import spider
from AMAZONscrapy.header_settings import matching_headers_obj
from scrapy.conf import settings
from ..settings import *
from AMA_ANALYSIS.Identify_country import identify_Country
from AMA_DATABASE.Remove_duplicate import remove_obj
from threading import Thread
import logging
from scrapy_redis.spiders import  RedisSpider



# class AmaSpidersSpider(scrapy.Spider):
class AmaSpidersSpider(RedisSpider):
    name = 'ama_spiders'
    # allowed_domains = []
    redis_key = 'start_url'
    start_urls = [
                'https://www.amazon.com/Hosa-YPP-118-inch-Dual-Cable/dp/B000068O56/ref=zg_bs_11973391_24?_encoding=UTF8&psc=1&refRID=H4DG103KV3PX2VJYAVH0'
                ]


    def parse(self, response):

        item = AmazonscrapyItem()
        item['response'] = response
        item['status_code'] = response.status
        yield item

    def start_requests(self):

        redis_obj = AmazonscrapyPipeline().open_spider(spider=spider)
        t = Thread(target=self.send_Status,args=(redis_obj,))
        t.deamon = True
        t.start()
        while True:
            try:
                while True:
                    if redis_obj.llen('product_info') > 5000:
                        time.sleep(5)
                    else:
                        break
                url = redis_obj.blpop(redis_start_url,0)[1].decode('utf8')
                if remove_obj.remove_Duplicate_ASIN_url(url=url)[0]:

                    Country = identify_Country(url=url)
                    # 这里的 Country 上下对应， 由　url域名后缀　进过判断后的对应国家的简称，不同于product_info 里面的　Country
                    headers = matching_headers_obj.matching_Header(url=url, Country=Country)
                    # print('headers:', headers)
                    print(url)
                    yield scrapy.Request(url=url, callback=self.parse,headers=headers,dont_filter=False)
                    # time.sleep(0.5)

            except Exception as e:
                print(e)
                logging.exception('start_request')
                pass


    def send_Status(self,redis_obj):
        '''
        每十秒发送一次状态
        :return:
        '''
        while True:
            # print('状态发送程序启动')
            redis_obj.set(status_code,1,ex=10)
            print('status_code',status_code)
            print('starts_key',redis_start_url)
            print('pid',os.getpid())
            time.sleep(10)


