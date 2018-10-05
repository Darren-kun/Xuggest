# -*- coding: utf-8 -*-

# Scrapy settings for AMAZONscrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'AMAZONscrapy'

SPIDER_MODULES = ['AMAZONscrapy.spiders']
NEWSPIDER_MODULE = 'AMAZONscrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'AMAZONscrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 64

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
      ##英国的ｃｏｏｋｉｅ
    # 'cookie': 'at-acbuk=Atza|IwEBILB65q8rA2KSv-Y8WFXWgH0UgGbtkWh138wiqt30gBmlJoFVqHF-RB_cziU8xf97HVVgoc7PHRJVcHvnz200wg5jUAdPozEskgo7DdZTgPMKSK-grfbbN3EZIGfcWEuok2g-diK2jy8OggRAt8k5ej_ZwR4MS6w1NDI0N25OaqU9gOq7WRak4khdNV1z7cSlOVR5vRDbIN4EoBlCzn3TfLROmwUYMOwp1OAWCxZniWqU3_UEjJgBLu-BF5awXhVmjWrh2VFm2Oeg87c40AZxIppx0T6hMB-Ap8OScBubGE0BtdG44RLbUZX7PMj-MiTd1i9qhqvybdatVFrGQaAM2BZMOpfYDntKyI2-otvFkqln7_Q1yqNsJ4zozlXL4oMTgMVpDybUm8TrHiiPdTrlZETX; sess-at-acbuk="Nuv2g/dTPhm4YjP6mh6hUAAm6VgZP3p/hJdAnRcadr0="; sst-acbuk=Sst1|PQGsOeWO2qEow4NwlQj1gOY5Cxj5QlTHhg-L3rcs9PAvIYbb710RcSF_p551DagxfFp0LHldbQQ0mJ04YTg8pEG_KurLjd05IWRE6LD1k2-2QfmsRPwWbhtfq7DLc-IZxVWSL2TE9a47-owVudIUUbUd3YQddFNoGkM1x4MDEOe3uOP06flbRZ-f416a7nh2WBb477ll2Otiy5wlU0nGTRktmiRh9WHfx5j_9T7XXTgKbARSiPFNniIWitk5dGNiDPz44McutLcLni1rgO-olN4krQoNsm_7rchji9lTG3AIJv9A_LRLQCbRadwgmbUj3_hJHepFXc-OP9NLnmYhCA1Kzw; x-wl-uid=1muHCEEwwEyWq0VHosiHEIhK+KteZZdxwOkO8RB4DzUorsFMkQxLiwMDY4bOkZPTcwezTMn0zV15TFgEPZEOkCg==; lc-acbuk=en_GB; session-token="HDO2XErJEEaH7lXXCpHmpW20KJxj7Lc4kCX8Rza8XNbNaheYZpjBLvzWe441Dahk62ldVDBKlkwXpt2fjovV2T+VXjdzdfmasz8qOEvpI/lBxH3q7zcGBBvXoUndwANqwjLfTkueRG7ytHbYCZhmZzg71bUmUwzLyjVpRhCdrwUFilD0iJvMoMvmp5jpZwLIFqf86iYySlhdjc0RtmdmnjSTPXgvIhQpENd/6q1upcsEaC0slDM81DgYHDgGdI003Cym6mv6ZWE9DycL66sK9w=="; x-acbuk="74P@bJpcWxl2tNk6mUvBXgxPaT8YlslXrwRwXIG5y3woZtzlLTWe1d33@w46RcCL"; csm-hit=tb:0NR6843RBJBQ97858B5K+b-03P2H4ND3FZYE949G8XQ|1537450264552&adb:adblk_no&t:1537450264552; ubid-acbuk=259-2948611-7840936; session-id-time=2082758401l; session-id=259-1136416-4224409',
    # 'cookie': 'at-acbuk=Atza|IwEBILB65q8rA2KSv-Y8WFXWgH0UgGbtkWh138wiqt30gBmlJoFVqHF-RB_cziU8xf97HVVgoc7PHRJVcHvnz200wg5jUAdPozEskgo7DdZTgPMKSK-grfbbN3EZIGfcWEuok2g-diK2jy8OggRAt8k5ej_ZwR4MS6w1NDI0N25OaqU9gOq7WRak4khdNV1z7cSlOVR5vRDbIN4EoBlCzn3TfLROmwUYMOwp1OAWCxZniWqU3_UEjJgBLu-BF5awXhVmjWrh2VFm2Oeg87c40AZxIppx0T6hMB-Ap8OScBubGE0BtdG44RLbUZX7PMj-MiTd1i9qhqvybdatVFrGQaAM2BZMOpfYDntKyI2-otvFkqln7_Q1yqNsJ4zozlXL4oMTgMVpDybUm8TrHiiPdTrlZETX; sess-at-acbuk="Nuv2g/dTPhm4YjP6mh6hUAAm6VgZP3p/hJdAnRcadr0="; sst-acbuk=Sst1|PQGsOeWO2qEow4NwlQj1gOY5Cxj5QlTHhg-L3rcs9PAvIYbb710RcSF_p551DagxfFp0LHldbQQ0mJ04YTg8pEG_KurLjd05IWRE6LD1k2-2QfmsRPwWbhtfq7DLc-IZxVWSL2TE9a47-owVudIUUbUd3YQddFNoGkM1x4MDEOe3uOP06flbRZ-f416a7nh2WBb477ll2Otiy5wlU0nGTRktmiRh9WHfx5j_9T7XXTgKbARSiPFNniIWitk5dGNiDPz44McutLcLni1rgO-olN4krQoNsm_7rchji9lTG3AIJv9A_LRLQCbRadwgmbUj3_hJHepFXc-OP9NLnmYhCA1Kzw; x-wl-uid=1muHCEEwwEyWq0VHosiHEIhK+KteZZdxwOkO8RB4DzUorsFMkQxLiwMDY4bOkZPTcwezTMn0zV15TFgEPZEOkCg==; lc-acbuk=en_GB; session-token="KsjiP+vMjh2+HKYJBJocO7EW6URuxY/iykJsQg9FqEHnjOnRC3QcObjjEyFav7cqtn78x4qJx7R/8XPNRSzluQu6nyUdxOSvCeqK9URNiI2x3wqIGgoxrf+MJ05RlBCS2yn1l7EoLKeVTqwk3FzZweTKBc33xaaX81JexVeTvKCp8B+vn7Qs5fPNuqeMpcQjGnjEr52aSoFTr56BZdtVwWDYzCFuVs/OPmgKoGEz9oqfy3qFCh+42ttjWpAYkUz6KwoFoP2K3DmK+38aGcQVOQ=="; x-acbuk="74P@bJpcWxl2tNk6mUvBXgxPaT8YlslXrwRwXIG5y3woZtzlLTWe1d33@w46RcCL"; csm-hit=tb:s-F6T2BQRVC980NJ08D1BG|1538031846192&adb:adblk_no&t:1538031847255; ubid-acbuk=259-2948611-7840936; session-id-time=2082758401l; session-id=259-1136416-4224409',
      ##美国的ｃｏｏｋｉｅ
    # 'cookie':'aws-priv=eyJ2IjoxLCJzdCI6MX0=; aws-ubid-main=726-4322876-5264241; __utma=194891197.616205732.1536288563.1536288563.1536299603.2; __utmz=194891197.1536299603.2.2.utmccn=(referral)|utmcsr=google.com.hk|utmcct=/|utmcmd=referral; at-main=Atza|IwEBIPgF-AE_KDXxI5YaQv7RD5roj54EnpO0CIg4QfhulqNORrlFGaCzaB1WGMP1xTF05aD7iz1wX-k_auZ0mN0XnSUjUBQdQK8KkPOyzY8C5iw8odCWvvvBHV98qXOp2A7adnKaoPHg7xWQ2bAbkdY1KPw3hxCfd30Z4IeYwUAnQI8Ce3FDbNCxPG3EoxtRJtxblH43sePtNUtMje1l8XSUug-lJzHmrttf3fLFuNj0DjdscDn3fyI9_PT_0FCJU1B84zkM1LYLBTF0UmPIFM3W9veVyQS9qtTHZcuoOtb7PRtlhqr3nAoOVgAYUw4EZlNTLzdgW1K1-ceMOXtTOQOZcARmzrokw99OP1xTNeWBqiu-J5rV66xaQfmkcv5j-xKCGW6RuBW489aNiKsw3r0XKOBDemn0xo1_LEN_CG7wLpY3_T0kjRLS2ByS0owxUfeJREw; sess-at-main="ZaYVj5l0CNqFyre77ea1d/H3xr5iJ65050JzoOUxncc="; sst-main=Sst1|PQHRsPPCDFKNMFn-A1FvRu0xFAJp8K6N6kr28c7d0JXEvayJORjl7PAgnBsKyXCEKg7h6j3oTgss0rcDxxa4vKDe8MQ3tFk1XU_FsGHhHbGsx0HzDuSR82kJqyX7pwGIzJazrKyD6ewuomCWwSpbDZS579ivM9HGnaQJwOLTcbO1QtCCRChvXSzd4nG1lzdDaz6SbNDTP0EopIQDdvJN8ippUB8wEhIAZjXtcIcpAcOtL2-aBF7b3umD6F5JZ_sMvHr95Qd02Ed7hV_TEi_vv0ZpsCn7s6Y1GDaEAL7N1gwhy4ZJHRzHB56N-5P4vVivfXFQyi1Z55MHwJMHRLTVahRxFNtIStaQ-p_FoVuChWL7OAwpVL-kvM-O2Oxo2m1v8BJZ2RZIL1EzcefHocqIV0sbMBuUeUmeM-Gzyqf1Ig3Fk7qzIc1fyFnT6G9zjtsZ2aHojxFxheHg0qtdrJ7h6l3Kvjzb-XF6xc26pKHmreqcszkKZKGVwnzZXEIovE2sNQZFbvBj_LPQYXi4igFS1sLIHg; x-wl-uid=1nNhPl/lMNoCyTp52iXW0o5yRZZY0hPWsbW+VNMUFw61B61bo00S8jHThY2x4NXYKjJWPN5UVvVr9ZK6IFKmCp0IG/0UGdd5K37oePW+d4mxH0QI5Yz2D0AHG4fK9zpO2MJnyXY+CH4o=; s_vn=1567824131517%26vn%3D6; s_fid=2523B29E269B79AA-2433F8EDAAAB4D24; s_dslv=1536653445983; s_nr=1536653447066-Repeat; regStatus=pre-register; session-token="17aGgIHRzXfDmdb8NXlVAYxB4raUH0v7IK0sHKAaoxIDQibNI6TEhymiEzY86lApQM3Pu0ScLasEoJaV0naO+GRGiLvl4xHOehGZ55JhupShd9bUJ+Wov1345IWUJfTwfbaJjxJ4M47Kp58d6WB7S0aGx9ZVkxEEYrM3oI4XapOOsBRn8S3mK9a5G9cprcgGWGLJur23KTdwVdEiEvl969OK8KmDdqgTf5MaMoc8ZtNzTznxVoXjFgXSFKj4ljG7MN1xD4xGdstIr0DSwSJAYw=="; x-main="lh36KXCBzvgIyZzx@zO7fZYNB6kIqbsoMY3ai44uyBFun3YbOMSAf0MKvBhW2UII"; csm-hit=tb:MZ37787TQKPVHH66Z8Z4+s-CZHM0BMGTDNCWE7DPD1C|1538017607428&adb:adblk_no; ubid-main=135-4084135-6200554; session-id-time=2082787201l; session-id=131-7800367-6862714',
    'referer': 'https://www.amazon.com/Pound-Steel-Metal-Loading-Ramps/dp/B00KUKW1FM/ref=zg_bs_256393011_78?_encoding=UTF8&psc=1&refRID=ZVVSHY42P0VWYEGMW47N',
    'upgrade-insecure-requests': '1',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
}


# DEFAULT_REQUEST_HEADERS = {
# 'authority':'www.amazon.co.uk',
# :method:GET
# :path:/Watch-Band-SODIAL-Leather-Replacement/dp/B01LNFWNQY/ref=bbp_bb_939231_st_9XNr_w_1?psc=1&smid=ARKG530VO6V7A
# :scheme:https
# accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# accept-encoding:gzip, deflate, sdch
# accept-language:zh-CN,zh;q=0.8
# cache-control:max-age=0
# cookie:at-acbuk=Atza|IwEBILB65q8rA2KSv-Y8WFXWgH0UgGbtkWh138wiqt30gBmlJoFVqHF-RB_cziU8xf97HVVgoc7PHRJVcHvnz200wg5jUAdPozEskgo7DdZTgPMKSK-grfbbN3EZIGfcWEuok2g-diK2jy8OggRAt8k5ej_ZwR4MS6w1NDI0N25OaqU9gOq7WRak4khdNV1z7cSlOVR5vRDbIN4EoBlCzn3TfLROmwUYMOwp1OAWCxZniWqU3_UEjJgBLu-BF5awXhVmjWrh2VFm2Oeg87c40AZxIppx0T6hMB-Ap8OScBubGE0BtdG44RLbUZX7PMj-MiTd1i9qhqvybdatVFrGQaAM2BZMOpfYDntKyI2-otvFkqln7_Q1yqNsJ4zozlXL4oMTgMVpDybUm8TrHiiPdTrlZETX; sess-at-acbuk="Nuv2g/dTPhm4YjP6mh6hUAAm6VgZP3p/hJdAnRcadr0="; sst-acbuk=Sst1|PQGsOeWO2qEow4NwlQj1gOY5Cxj5QlTHhg-L3rcs9PAvIYbb710RcSF_p551DagxfFp0LHldbQQ0mJ04YTg8pEG_KurLjd05IWRE6LD1k2-2QfmsRPwWbhtfq7DLc-IZxVWSL2TE9a47-owVudIUUbUd3YQddFNoGkM1x4MDEOe3uOP06flbRZ-f416a7nh2WBb477ll2Otiy5wlU0nGTRktmiRh9WHfx5j_9T7XXTgKbARSiPFNniIWitk5dGNiDPz44McutLcLni1rgO-olN4krQoNsm_7rchji9lTG3AIJv9A_LRLQCbRadwgmbUj3_hJHepFXc-OP9NLnmYhCA1Kzw; x-wl-uid=1muHCEEwwEyWq0VHosiHEIhK+KteZZdxwOkO8RB4DzUorsFMkQxLiwMDY4bOkZPTcwezTMn0zV15TFgEPZEOkCg==; session-token="HDO2XErJEEaH7lXXCpHmpW20KJxj7Lc4kCX8Rza8XNbNaheYZpjBLvzWe441Dahk62ldVDBKlkwXpt2fjovV2T+VXjdzdfmasz8qOEvpI/lBxH3q7zcGBBvXoUndwANqwjLfTkueRG7ytHbYCZhmZzg71bUmUwzLyjVpRhCdrwUFilD0iJvMoMvmp5jpZwLIFqf86iYySlhdjc0RtmdmnjSTPXgvIhQpENd/6q1upcsEaC0slDM81DgYHDgGdI003Cym6mv6ZWE9DycL66sK9w=="; x-acbuk="74P@bJpcWxl2tNk6mUvBXgxPaT8YlslXrwRwXIG5y3woZtzlLTWe1d33@w46RcCL"; ubid-acbuk=259-2948611-7840936; session-id-time=2082758401l; lc-acbuk=en_GB; session-id=259-1136416-4224409; csm-hit=tb:R970CMBQQA08JJ90GS1M+s-R970CMBQQA08JJ90GS1M|1537451526501&adb:adblk_no&t:1537451526501
# upgrade-insecure-requests:1
# user-agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36
# }


# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'AMAZONscrapy.middlewares.AmazonscrapySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'AMAZONscrapy.middlewares.AmazonscrapyDownloaderMiddleware': 543,
    'AMAZONscrapy.middlewares.ProxyMiddleware':543
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'AMAZONscrapy.pipelines.AmazonscrapyPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

HTTPERROR_ALLOWED_CODES = [503]

DOWNLOAD_TIMEOUT = 20
# RETRY_ENABLED = 10

#重定向设置
# REDIRECT_ENABLED = False

#PROXIES = ['https://108.59.14.203:13040']
# PROXIES = ["https://108.59.14.208:13040",'https://108.59.14.203:13040']
#高级
#PROXIES = ['https://108.59.14.200:13152']
PROXIES = ['https://95.211.175.167:13150']
#PROXIES = ['https://108.59.14.203:13040','https://95.211.175.167:13150']
# REDIS_HOST = '104.128.86.133'
# REDIS_POST = 6379

#主爬虫连接的ｒｅｄｉｓ　ＰＯＳＴ　和　ＨＯＳＴ
REDIS_POST_HOST = {'HOST':'104.128.86.133','POST':6379}
REDIS_HOST = '104.128.86.133'
REDIS_PORT = 6379

#使用scrapy-redis里面的去重组件.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy-redis里面的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 允许暂停后,能保存进度
SCHEDULER_PERSIST = True
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'




# ama_spiders 爬虫的状态代号
status_code = 'status_104.128.86.133'
# ama_spiders_02 爬虫的状态代号
status_code_02 = 'status_104.128.86.133_02'

#在ｒｅｄｉｓ获取ｕｒｌ的ｋｅｙ
redis_start_url = 'start_url'

#在 redis 暂时存放＿product_info 的　ｋｅｙ　 　
submit_key = 'product_info'

#多进程获取信息后存入ｒｅｄｉｓ的顺序限制
pass_word = 'token'

#自定义的简单日志，用于记录子进程解析情况
ama_blog_filename = 'analysis_log.txt'


#开启日志
LOG_ENABLED = True
#设置日志输出等级
LOG_LEVEL = 'WARNING'

# 1. logging.CRITICAL - for critical errors (highest severity)
#
# 2. logging.ERROR - for regular errors
#
# 3. logging.WARNING - for warning messages
#
# 4. logging.INFO - for informational messages
#
# 5. logging.DEBUG - for debugging messages (lowest severity)
#写日志的格式
# logging.log(logging.INFO, 'log content')

#日志名
LOG_FILE = "AMAZONscrapy.log"
