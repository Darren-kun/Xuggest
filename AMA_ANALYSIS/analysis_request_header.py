# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:10:44 2018

@author: PC1
"""

# -*- coding: utf-8 -*-
import random

from ama_blog import logger

"""
Created on Wed Aug 29 14:39:51 2018

@author: Darren_KUN
"""

import requests
# from AMAZONscrapy.AMAZONscrapy.AMA_ANALYSIS_TEST.show_respones_html import show_responses_html
from AMA_ANALYSIS_TEST.show_respones_html import show_responses_html

##请求所需要的　proxies
proxies_list = [
                #{'https':'95.211.175.167:13150'},
		{'https':'108.59.14.200:13152'},
                ]

class HEASER_FORM_DATA():
    '''
    提供解析功能包　所有需要用到的请求头类型，和ＰＯＳＴ请求内容
    '''
    def USA_Add_cart_header(self):
        '''
        从商品详情页面，提交购物车时使用
        :return:
        '''
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'max-age=0',
            'cookie': 'x-wl-uid=18OFwwOgo1yq08sFZJRIeWYisOH8morTTb+XylBVl+C4n9C5FLAGN4d2sbjzQj1+KrWq1Q6TxZy8=; session-token=owbniuTqY8cRHUN93X8yK6GsKrrMuwigRGro7lN5aBkX5IADGZFrBSIJsy6+Rd8aO1CDzLv9l5bcrowEiC0Xs2FL60UFvuU7u0RVuFSdCMV+mgrrat5J6hvnw3htaSNVFMVlxviTqMiLpMxIwqgVCVyFX5khTQTEqPyv4OEwP2O388zACB0KVS6Hz5OPMfJY; ubid-main=135-4084135-6200554; session-id-time=2082787201l; session-id=131-7800367-6862714; csm-hit=tb:H2H5S3GV40FN9RKEY15K+b-9FQC9XX9BPZNNW31WXSR|1536033272985&adb:adblk_no',
            'referer': 'https://www.amazon.com/b/ref=s9_acss_bw_cg_HPCHCCT_2a1_w?_encoding=UTF8&node=3762591&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=merchandised-search-4&pf_rd_r=SSTHP77BH0765CGSCEH7&pf_rd_r=SSTHP77BH0765CGSCEH7&pf_rd_t=101&pf_rd_p=a06e98c9-041b-5b5f-8706-e60ae7ff1aa2&pf_rd_p=a06e98c9-041b-5b5f-8706-e60ae7ff1aa2&pf_rd_i=3760941',
            'upgrade-insecure-requests': '1',
            'user-agent': user_agent
        }
        return headers

    def USA_Sellers_list_Header(self):
        '''
        进入seller 列表页面
        :return:
        '''

        headers = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, sdch',
            'accept-language':'zh-CN,zh;q=0.8',
            'cookie':'aws-priv=eyJ2IjoxLCJzdCI6MX0=; aws-ubid-main=726-4322876-5264241; __utma=194891197.616205732.1536288563.1536288563.1536299603.2; __utmc=194891197; __utmz=194891197.1536299603.2.2.utmccn=(referral)|utmcsr=google.com.hk|utmcct=/|utmcmd=referral; at-main=Atza|IwEBIPgF-AE_KDXxI5YaQv7RD5roj54EnpO0CIg4QfhulqNORrlFGaCzaB1WGMP1xTF05aD7iz1wX-k_auZ0mN0XnSUjUBQdQK8KkPOyzY8C5iw8odCWvvvBHV98qXOp2A7adnKaoPHg7xWQ2bAbkdY1KPw3hxCfd30Z4IeYwUAnQI8Ce3FDbNCxPG3EoxtRJtxblH43sePtNUtMje1l8XSUug-lJzHmrttf3fLFuNj0DjdscDn3fyI9_PT_0FCJU1B84zkM1LYLBTF0UmPIFM3W9veVyQS9qtTHZcuoOtb7PRtlhqr3nAoOVgAYUw4EZlNTLzdgW1K1-ceMOXtTOQOZcARmzrokw99OP1xTNeWBqiu-J5rV66xaQfmkcv5j-xKCGW6RuBW489aNiKsw3r0XKOBDemn0xo1_LEN_CG7wLpY3_T0kjRLS2ByS0owxUfeJREw; sess-at-main="ZaYVj5l0CNqFyre77ea1d/H3xr5iJ65050JzoOUxncc="; sst-main=Sst1|PQHRsPPCDFKNMFn-A1FvRu0xFAJp8K6N6kr28c7d0JXEvayJORjl7PAgnBsKyXCEKg7h6j3oTgss0rcDxxa4vKDe8MQ3tFk1XU_FsGHhHbGsx0HzDuSR82kJqyX7pwGIzJazrKyD6ewuomCWwSpbDZS579ivM9HGnaQJwOLTcbO1QtCCRChvXSzd4nG1lzdDaz6SbNDTP0EopIQDdvJN8ippUB8wEhIAZjXtcIcpAcOtL2-aBF7b3umD6F5JZ_sMvHr95Qd02Ed7hV_TEi_vv0ZpsCn7s6Y1GDaEAL7N1gwhy4ZJHRzHB56N-5P4vVivfXFQyi1Z55MHwJMHRLTVahRxFNtIStaQ-p_FoVuChWL7OAwpVL-kvM-O2Oxo2m1v8BJZ2RZIL1EzcefHocqIV0sbMBuUeUmeM-Gzyqf1Ig3Fk7qzIc1fyFnT6G9zjtsZ2aHojxFxheHg0qtdrJ7h6l3Kvjzb-XF6xc26pKHmreqcszkKZKGVwnzZXEIovE2sNQZFbvBj_LPQYXi4igFS1sLIHg; _rails-root_session=Mk5oaFJiWWZxTkRzNWlsaU50dHZNb3N1bGM1eS9hYWZLcTR5SjBqZElKMkJXRXJqaVBHNkZsTU5HU01lejhzVnR0UytUWmNGRzV4QTdiR1hXUEVpVyt1SVN4bmpGbENHckxRQXk3L0Fnbm9PZ040cVdYd2pEOVV2OFBDWWNPTUlKNERPdE9TSU1OK2FTNjF0QlRGWTNVUG5weW02ZHJ1VmpiKzFuaDNDYS9rKytkSlM4SlZ0cmlibVlreXN1dHlJLS1HOTVlVHhLOG1OWTFkMjU0WFlmRkZnPT0%3D--d6777b9ce913a9797f1fb473aa314415d77cc525; s_sq=%5B%5BB%5D%5D; s_cc=true; x-wl-uid=1nNhPl/lMNoCyTp52iXW0o5yRZZY0hPWsbW+VNMUFw61B61bo00S8jHThY2x4NXYKjJWPN5UVvVr9ZK6IFKmCp0IG/0UGdd5K37oePW+d4mxH0QI5Yz2D0AHG4fK9zpO2MJnyXY+CH4o=; x-main="lh36KXCBzvgIyZzx@zO7fZYNB6kIqbsoMY3ai44uyBFun3YbOMSAf0MKvBhW2UII"; s_vn=1567824131517%26vn%3D6; c_m=undefinedwww.google.comSearch%20Engine; s_fid=2523B29E269B79AA-2433F8EDAAAB4D24; s_dslv=1536653445983; s_nr=1536653447066-Repeat; regStatus=pre-register; skin=noskin; session-token=OQxZcCyjRRNIjaHASuroCbIsg7FaIolTBBUjbTe3F5KEDMoxpZWFn/0JcyBTcar5gYVHcP2noAjagRTqyR95JSGGf4PlAXcNVfigJcuQvrGpNp6j9Qq36qJs0NUB3jC0kiVDCRkqZuk1meJR5Bk93XSsq27wZEPPn3aYts44ArLUJmJdsAhvwee2+R4lFqzyu2HiOoTZ0P8c6BBMBjhvNJtzfNdnJRsjybMIQ5ihKoh27id/abx05Ry+Tn2jONpCJa6JiTrEqw/lFuMK+lqjbg==; ubid-main=135-4084135-6200554; session-id-time=2082787201l; session-id=131-7800367-6862714; csm-hit=tb:PB9HSTDSQ6K5DFWSRC7R+b-VMEF06TW7XB91HP2P8BN|1536802850339&adb:adblk_no',
            #测试结果　referer 这个参数　不影响结果
            # 'referer':'https://www.amazon.com/Avanti-RA7316PST-Apartment-Refrigerator-Platinum/dp/B00D1SZNO6',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'
        }
        return headers

    def USA_Sellers_list_addcart_Header(self):
        '''
        在卖家列表里　添加购物车所使用的　请求头
        :return:
        '''
        headers = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding':'gzip, deflate',
            'accept-language':'zh-CN,zh;q=0.8',
            'cache-control':'max-age=0',
            'content-length':'347',
            'content-type':'application/x-www-form-urlencoded',

            # 'cookie':'aws-priv=eyJ2IjoxLCJzdCI6MX0=; aws-ubid-main=726-4322876-5264241; __utma=194891197.616205732.1536288563.1536288563.1536299603.2; __utmc=194891197; __utmz=194891197.1536299603.2.2.utmccn=(referral)|utmcsr=google.com.hk|utmcct=/|utmcmd=referral; at-main=Atza|IwEBIPgF-AE_KDXxI5YaQv7RD5roj54EnpO0CIg4QfhulqNORrlFGaCzaB1WGMP1xTF05aD7iz1wX-k_auZ0mN0XnSUjUBQdQK8KkPOyzY8C5iw8odCWvvvBHV98qXOp2A7adnKaoPHg7xWQ2bAbkdY1KPw3hxCfd30Z4IeYwUAnQI8Ce3FDbNCxPG3EoxtRJtxblH43sePtNUtMje1l8XSUug-lJzHmrttf3fLFuNj0DjdscDn3fyI9_PT_0FCJU1B84zkM1LYLBTF0UmPIFM3W9veVyQS9qtTHZcuoOtb7PRtlhqr3nAoOVgAYUw4EZlNTLzdgW1K1-ceMOXtTOQOZcARmzrokw99OP1xTNeWBqiu-J5rV66xaQfmkcv5j-xKCGW6RuBW489aNiKsw3r0XKOBDemn0xo1_LEN_CG7wLpY3_T0kjRLS2ByS0owxUfeJREw; sess-at-main="ZaYVj5l0CNqFyre77ea1d/H3xr5iJ65050JzoOUxncc="; sst-main=Sst1|PQHRsPPCDFKNMFn-A1FvRu0xFAJp8K6N6kr28c7d0JXEvayJORjl7PAgnBsKyXCEKg7h6j3oTgss0rcDxxa4vKDe8MQ3tFk1XU_FsGHhHbGsx0HzDuSR82kJqyX7pwGIzJazrKyD6ewuomCWwSpbDZS579ivM9HGnaQJwOLTcbO1QtCCRChvXSzd4nG1lzdDaz6SbNDTP0EopIQDdvJN8ippUB8wEhIAZjXtcIcpAcOtL2-aBF7b3umD6F5JZ_sMvHr95Qd02Ed7hV_TEi_vv0ZpsCn7s6Y1GDaEAL7N1gwhy4ZJHRzHB56N-5P4vVivfXFQyi1Z55MHwJMHRLTVahRxFNtIStaQ-p_FoVuChWL7OAwpVL-kvM-O2Oxo2m1v8BJZ2RZIL1EzcefHocqIV0sbMBuUeUmeM-Gzyqf1Ig3Fk7qzIc1fyFnT6G9zjtsZ2aHojxFxheHg0qtdrJ7h6l3Kvjzb-XF6xc26pKHmreqcszkKZKGVwnzZXEIovE2sNQZFbvBj_LPQYXi4igFS1sLIHg; _rails-root_session=Mk5oaFJiWWZxTkRzNWlsaU50dHZNb3N1bGM1eS9hYWZLcTR5SjBqZElKMkJXRXJqaVBHNkZsTU5HU01lejhzVnR0UytUWmNGRzV4QTdiR1hXUEVpVyt1SVN4bmpGbENHckxRQXk3L0Fnbm9PZ040cVdYd2pEOVV2OFBDWWNPTUlKNERPdE9TSU1OK2FTNjF0QlRGWTNVUG5weW02ZHJ1VmpiKzFuaDNDYS9rKytkSlM4SlZ0cmlibVlreXN1dHlJLS1HOTVlVHhLOG1OWTFkMjU0WFlmRkZnPT0%3D--d6777b9ce913a9797f1fb473aa314415d77cc525; s_sq=%5B%5BB%5D%5D; s_cc=true; x-wl-uid=1nNhPl/lMNoCyTp52iXW0o5yRZZY0hPWsbW+VNMUFw61B61bo00S8jHThY2x4NXYKjJWPN5UVvVr9ZK6IFKmCp0IG/0UGdd5K37oePW+d4mxH0QI5Yz2D0AHG4fK9zpO2MJnyXY+CH4o=; x-main="lh36KXCBzvgIyZzx@zO7fZYNB6kIqbsoMY3ai44uyBFun3YbOMSAf0MKvBhW2UII"; s_vn=1567824131517%26vn%3D6; c_m=undefinedwww.google.comSearch%20Engine; s_fid=2523B29E269B79AA-2433F8EDAAAB4D24; s_dslv=1536653445983; s_nr=1536653447066-Repeat; regStatus=pre-register; skin=noskin; session-token=n31TY6z6w4VF0dQKb8qfSrNzBCK3Dj6PJY3WYe/u4Rfiu/+/aAz39WEJa6Ta/lCDBH3evpfXZlznDPG041oAfazBjDE6L1b1B5jNKsDnqu6BWsDzS9XF/l1E4I/z1L4JFeYfM9IepLVUQZJMhDWll5StmyzoLULtjQjqYZTofUWYWI7D2OpaSOM4aVRZrlRbrK4GLmDAP5/q1ax5pEmwWpkNF5U8x0WElPeG1W90dVxo3zDATsa3Dcs5j7tCA5UHyMU1e9RoC1WdB1Ny1fe9Yw==; csm-hit=tb:PB9HSTDSQ6K5DFWSRC7R+s-784X7RZCK6EGYKB7WTRH|1536808709544&adb:adblk_no; ubid-main=135-4084135-6200554; session-id-time=2082787201l; session-id=131-7800367-6862714',
            ##替换cookie测试(X)
            'cookie':'aws-priv=eyJ2IjoxLCJzdCI6MX0=; aws-ubid-main=726-4322876-5264241; __utma=194891197.616205732.1536288563.1536288563.1536299603.2; __utmc=194891197; __utmz=194891197.1536299603.2.2.utmccn=(referral)|utmcsr=google.com.hk|utmcct=/|utmcmd=referral; at-main=Atza|IwEBIPgF-AE_KDXxI5YaQv7RD5roj54EnpO0CIg4QfhulqNORrlFGaCzaB1WGMP1xTF05aD7iz1wX-k_auZ0mN0XnSUjUBQdQK8KkPOyzY8C5iw8odCWvvvBHV98qXOp2A7adnKaoPHg7xWQ2bAbkdY1KPw3hxCfd30Z4IeYwUAnQI8Ce3FDbNCxPG3EoxtRJtxblH43sePtNUtMje1l8XSUug-lJzHmrttf3fLFuNj0DjdscDn3fyI9_PT_0FCJU1B84zkM1LYLBTF0UmPIFM3W9veVyQS9qtTHZcuoOtb7PRtlhqr3nAoOVgAYUw4EZlNTLzdgW1K1-ceMOXtTOQOZcARmzrokw99OP1xTNeWBqiu-J5rV66xaQfmkcv5j-xKCGW6RuBW489aNiKsw3r0XKOBDemn0xo1_LEN_CG7wLpY3_T0kjRLS2ByS0owxUfeJREw; sess-at-main="ZaYVj5l0CNqFyre77ea1d/H3xr5iJ65050JzoOUxncc="; sst-main=Sst1|PQHRsPPCDFKNMFn-A1FvRu0xFAJp8K6N6kr28c7d0JXEvayJORjl7PAgnBsKyXCEKg7h6j3oTgss0rcDxxa4vKDe8MQ3tFk1XU_FsGHhHbGsx0HzDuSR82kJqyX7pwGIzJazrKyD6ewuomCWwSpbDZS579ivM9HGnaQJwOLTcbO1QtCCRChvXSzd4nG1lzdDaz6SbNDTP0EopIQDdvJN8ippUB8wEhIAZjXtcIcpAcOtL2-aBF7b3umD6F5JZ_sMvHr95Qd02Ed7hV_TEi_vv0ZpsCn7s6Y1GDaEAL7N1gwhy4ZJHRzHB56N-5P4vVivfXFQyi1Z55MHwJMHRLTVahRxFNtIStaQ-p_FoVuChWL7OAwpVL-kvM-O2Oxo2m1v8BJZ2RZIL1EzcefHocqIV0sbMBuUeUmeM-Gzyqf1Ig3Fk7qzIc1fyFnT6G9zjtsZ2aHojxFxheHg0qtdrJ7h6l3Kvjzb-XF6xc26pKHmreqcszkKZKGVwnzZXEIovE2sNQZFbvBj_LPQYXi4igFS1sLIHg; _rails-root_session=Mk5oaFJiWWZxTkRzNWlsaU50dHZNb3N1bGM1eS9hYWZLcTR5SjBqZElKMkJXRXJqaVBHNkZsTU5HU01lejhzVnR0UytUWmNGRzV4QTdiR1hXUEVpVyt1SVN4bmpGbENHckxRQXk3L0Fnbm9PZ040cVdYd2pEOVV2OFBDWWNPTUlKNERPdE9TSU1OK2FTNjF0QlRGWTNVUG5weW02ZHJ1VmpiKzFuaDNDYS9rKytkSlM4SlZ0cmlibVlreXN1dHlJLS1HOTVlVHhLOG1OWTFkMjU0WFlmRkZnPT0%3D--d6777b9ce913a9797f1fb473aa314415d77cc525; s_sq=%5B%5BB%5D%5D; s_cc=true; x-wl-uid=1nNhPl/lMNoCyTp52iXW0o5yRZZY0hPWsbW+VNMUFw61B61bo00S8jHThY2x4NXYKjJWPN5UVvVr9ZK6IFKmCp0IG/0UGdd5K37oePW+d4mxH0QI5Yz2D0AHG4fK9zpO2MJnyXY+CH4o=; x-main="lh36KXCBzvgIyZzx@zO7fZYNB6kIqbsoMY3ai44uyBFun3YbOMSAf0MKvBhW2UII"; s_vn=1567824131517%26vn%3D6; c_m=undefinedwww.google.comSearch%20Engine; s_fid=2523B29E269B79AA-2433F8EDAAAB4D24; s_dslv=1536653445983; s_nr=1536653447066-Repeat; regStatus=pre-register; skin=noskin; session-token="tF9dkWC1HSZdpH1Vnk0gboZHXIIqqDy5zciIQhbZBW+TZyhIp9IDPGav91wcwIzuwbnXqQV+My8BuAoikwLCUjyzxSHvIEohOQIH8O2WB9/1qlu8JDerO6+ApSySksCIMQJpcqUHmlaR6cMVdoE7Hl2+2n9FlkJarVJxolXWZF4ZkDiSv/Xn5BckzsCfKoChTtrulMUTLVq4z0jIc5m3k0xL+93qszpR6BvgubhvDMOYE2iLXLQRqZ4IE4xLmaZufDn0uiTRS75wLVMQ2OBCjg=="; ubid-main=135-4084135-6200554; session-id-time=2082787201l; session-id=131-7800367-6862714; csm-hit=tb:QNDGB2WZS8V79NGYCAE9+s-BN24BWJP5CBG70JCWCC3|1536814734417&adb:adblk_no',
            'origin':'https://www.amazon.com',
            ##不影响　请求结果
            # 'referer':'https://www.amazon.com/gp/offer-listing/B00D1SZNO6/ref=dp_olp_new_mbc?ie=UTF8&condition=new',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'

        }

        return headers

    def USA_updata_Shopping_nub_Header(self):
        '''
        在购物车　修改　购买数量时使用　的请求头
        :return:
        '''
        headers = {
            'accept':'application/json, text/javascript, */*; q=0.01',
            'accept-encoding':'gzip, deflate',
            'accept-language':'zh-CN,zh;q=0.8',
            'content-length':'1705',
            'content-type':'application/x-www-form-urlencoded; charset=UTF-8;',
            'cookie':'aws-priv=eyJ2IjoxLCJzdCI6MX0=; aws-ubid-main=726-4322876-5264241; __utma=194891197.616205732.1536288563.1536288563.1536299603.2; __utmc=194891197; __utmz=194891197.1536299603.2.2.utmccn=(referral)|utmcsr=google.com.hk|utmcct=/|utmcmd=referral; at-main=Atza|IwEBIPgF-AE_KDXxI5YaQv7RD5roj54EnpO0CIg4QfhulqNORrlFGaCzaB1WGMP1xTF05aD7iz1wX-k_auZ0mN0XnSUjUBQdQK8KkPOyzY8C5iw8odCWvvvBHV98qXOp2A7adnKaoPHg7xWQ2bAbkdY1KPw3hxCfd30Z4IeYwUAnQI8Ce3FDbNCxPG3EoxtRJtxblH43sePtNUtMje1l8XSUug-lJzHmrttf3fLFuNj0DjdscDn3fyI9_PT_0FCJU1B84zkM1LYLBTF0UmPIFM3W9veVyQS9qtTHZcuoOtb7PRtlhqr3nAoOVgAYUw4EZlNTLzdgW1K1-ceMOXtTOQOZcARmzrokw99OP1xTNeWBqiu-J5rV66xaQfmkcv5j-xKCGW6RuBW489aNiKsw3r0XKOBDemn0xo1_LEN_CG7wLpY3_T0kjRLS2ByS0owxUfeJREw; sess-at-main="ZaYVj5l0CNqFyre77ea1d/H3xr5iJ65050JzoOUxncc="; sst-main=Sst1|PQHRsPPCDFKNMFn-A1FvRu0xFAJp8K6N6kr28c7d0JXEvayJORjl7PAgnBsKyXCEKg7h6j3oTgss0rcDxxa4vKDe8MQ3tFk1XU_FsGHhHbGsx0HzDuSR82kJqyX7pwGIzJazrKyD6ewuomCWwSpbDZS579ivM9HGnaQJwOLTcbO1QtCCRChvXSzd4nG1lzdDaz6SbNDTP0EopIQDdvJN8ippUB8wEhIAZjXtcIcpAcOtL2-aBF7b3umD6F5JZ_sMvHr95Qd02Ed7hV_TEi_vv0ZpsCn7s6Y1GDaEAL7N1gwhy4ZJHRzHB56N-5P4vVivfXFQyi1Z55MHwJMHRLTVahRxFNtIStaQ-p_FoVuChWL7OAwpVL-kvM-O2Oxo2m1v8BJZ2RZIL1EzcefHocqIV0sbMBuUeUmeM-Gzyqf1Ig3Fk7qzIc1fyFnT6G9zjtsZ2aHojxFxheHg0qtdrJ7h6l3Kvjzb-XF6xc26pKHmreqcszkKZKGVwnzZXEIovE2sNQZFbvBj_LPQYXi4igFS1sLIHg; _rails-root_session=Mk5oaFJiWWZxTkRzNWlsaU50dHZNb3N1bGM1eS9hYWZLcTR5SjBqZElKMkJXRXJqaVBHNkZsTU5HU01lejhzVnR0UytUWmNGRzV4QTdiR1hXUEVpVyt1SVN4bmpGbENHckxRQXk3L0Fnbm9PZ040cVdYd2pEOVV2OFBDWWNPTUlKNERPdE9TSU1OK2FTNjF0QlRGWTNVUG5weW02ZHJ1VmpiKzFuaDNDYS9rKytkSlM4SlZ0cmlibVlreXN1dHlJLS1HOTVlVHhLOG1OWTFkMjU0WFlmRkZnPT0%3D--d6777b9ce913a9797f1fb473aa314415d77cc525; s_sq=%5B%5BB%5D%5D; s_cc=true; x-wl-uid=1nNhPl/lMNoCyTp52iXW0o5yRZZY0hPWsbW+VNMUFw61B61bo00S8jHThY2x4NXYKjJWPN5UVvVr9ZK6IFKmCp0IG/0UGdd5K37oePW+d4mxH0QI5Yz2D0AHG4fK9zpO2MJnyXY+CH4o=; x-main="lh36KXCBzvgIyZzx@zO7fZYNB6kIqbsoMY3ai44uyBFun3YbOMSAf0MKvBhW2UII"; s_vn=1567824131517%26vn%3D6; c_m=undefinedwww.google.comSearch%20Engine; s_fid=2523B29E269B79AA-2433F8EDAAAB4D24; s_dslv=1536653445983; s_nr=1536653447066-Repeat; regStatus=pre-register; skin=noskin; session-token=n31TY6z6w4VF0dQKb8qfSrNzBCK3Dj6PJY3WYe/u4Rfiu/+/aAz39WEJa6Ta/lCDBH3evpfXZlznDPG041oAfazBjDE6L1b1B5jNKsDnqu6BWsDzS9XF/l1E4I/z1L4JFeYfM9IepLVUQZJMhDWll5StmyzoLULtjQjqYZTofUWYWI7D2OpaSOM4aVRZrlRbrK4GLmDAP5/q1ax5pEmwWpkNF5U8x0WElPeG1W90dVxo3zDATsa3Dcs5j7tCA5UHyMU1e9RoC1WdB1Ny1fe9Yw==; csm-hit=tb:Z8RXJYZVB6XGBHKY45M0+sa-7GS8KHXD1FBWX83ZAXFF-R5HRRG6PGSHKCAGWQ4H5|1536810158380&adb:adblk_no; ubid-main=135-4084135-6200554; session-id-time=2082787201l; session-id=131-7800367-6862714',
            'origin':'https://www.amazon.com',
            'referer':'https://www.amazon.com/gp/cart/view.html?ref=nav_cart',
            'user-agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
            'x-aui-view':'Desktop',
            'x-requested-with':'XMLHttpRequest'
        }
        return headers


    def from_Data(self,ASIN,offerListingID):
        '''
        在商品详情页处　添加购物车所用的　提交参数
        :param ASIN:
        :param offerListingID:
        :return:
        '''
        form_data = {
        'session-id':'131-7800367-6862714',
        'ASIN':ASIN,
        'offerListingID':offerListingID,
        'merchantID':'AU7HRQ5QS7YQX',
        'nodeID':'228013',
        'sellingCustomerID':'AU7HRQ5QS7YQX',
        'tagActionCode':'228013',
        'quantity':99999,
        'submit.add-to-cart':'Add to Cart',
        'dropdown-selection':'add-new',
        'dropdown-selection-ubb':'add-new'
        }

        return form_data

    def form_Data_02(self,ASIN,offeringID):
        '''
        购物车修改　购买数量　的提交参数
        :param ASIN:
        :param offeringID:
        :return:
        '''
        form_data = {
        'hasMoreItems':'1',
        'timeStamp':'1536805110',
        'token':'gApYke2nPV4YFAFMyWY39oGOC59WHrG0Upp+RCcAAAAJAAAAAFuZyPZyYXcAAAAA',
        'requestID':'QDC304F6V3SRRET44HR0',
        'activeItems':'C6758cccc-dcb7-4896-827f-0eafc574ef91|0|0|1|373.85|||0||',
        ##不影响的参数
        # 'savedItems':'S7f610369-bb32-40fe-84be-75433536184a|9.99|0|',
        # 'savedItems':'S046b4ed4-716d-452f-af87-1d2ad4508855|9.99|0|',
        # 'savedItems':'S6cac277d-ec84-4ed8-8511-2a9a3bc038d8|32.9|0|',
        # 'savedItems':'S43b90464-5d4f-4f38-b978-9ce12ca7a4c3|35.14|0|',
        # 'savedItems':'S20e50afc-c0f6-4e1c-8292-17c5e18958ed|7.29|0|',
        # 'savedItems':'Se8b447cc-f68b-4143-a3d2-8999ea66bba3|6.99|0|',
        # 'savedItems':'Sf8643012-1d74-454b-9ba4-19b7f44b34d7|13.92|0|',
        # 'savedItems':'S9c1ce16b-3e7e-49de-bd07-0459d19b865e|9.99|0|',
        # 'savedItems':'S1de63da2-0c60-40fe-9ace-9f66b6115547|5.99|0|',
        # 'savedItems':'Sa5bf1f50-687a-4dc8-ab36-695cd77be635|12.99|0|',
        # 'addressId':'',
        # 'addressZip':'',
        'closeAddonUpsell':'1',
        'flcExpanded':'0',
        'quantity.C6758cccc-dcb7-4896-827f-0eafc574ef91':999,
        'pageAction':'update-quantity',
        'submit.update-quantity.C6758cccc-dcb7-4896-827f-0eafc574ef91':'1',
        'displayedSavedItemNum':10,
        # 'actionItemID':'C6758cccc-dcb7-4896-827f-0eafc574ef91',
        'actionItemID':'C8ef8c054-923d-4d99-b9ce-ba022aef9240',
        'actionType':'update-quantity',
        'asin':ASIN,
        ##重要参数
        'encodedOffering':offeringID
        }


        return form_data

    def form_Data_03(self,ASIN,offeringID):
        '''
        在卖家列表处添加　购物车　时所用　的　参数内容
        :return:
        '''
        form_data = {
            'session-id': '131-7800367-6862714',
            ##替换测试
            'qid': '',
            'sr': '',
            'signInToHUC': '0',
            ##不影响结果
            # 'metric-asin.B00D1SZNO6': '1',
            'registryItemID.1': '',
            'registryID.1': '',
            'itemCount': '１',
            ##重要参数
            'offeringID.1':offeringID,
            'isAddon': '1',
            'submit.addToCart': 'Add to cart'
        }

        return form_data

    def UK_Add_cart_form(self):
        '''
        英国　商品详情页面添加购物车的请求头
        :return:
        '''
        headers = {
            'session-id': '259-1136416-4224409',
            'ASIN': '6040791616',
            'offerListingID': 'Bszk%2BtsUFDGHaC7gGA4lvGNC%2BzV0IWzAJ6WRdIZIDJ1KUmqkIYkJmeKQWyNZeUZV1uYqn4w38inZny6XuscuQakqw9dkOVPkXB6D9yZxu%2BTXcClnQKXDhIuz6ndV87vC9sYV%2FCmUzPFN4W%2BPJRMKpg%3D%3D',
            'isMerchantExclusive': '0',
            'merchantID': 'A8WW5I1KB59WB',
            'isAddon': '0',
            'nodeID': '355005011',
            'sellingCustomerID': 'A8WW5I1KB59WB',
            'qid': '',
            'sr': '',
            'storeID': 'shoes',
            'tagActionCode': '355005011',
            'viewID': 'glance',
            'rebateId': '',
            'rsid': '259-1136416-4224409',
            'sourceCustomerOrgListID': '',
            'sourceCustomerOrgListItemID': '',
            'wlPopCommand': '',
            'quantity': 1,
            'submit.add-to-cart': 'Add to Basket',
            'dropdown-selection': 'add-new',
            'dropdown-selection-ubb': 'add-new'
        }

        return headers

        pass


##创建一个实例，获取对应的　请求头　或　提交参数　
header_form_data_obj = HEASER_FORM_DATA()

def myrequest_get(url,headers):
    '''
    utf8 的ｒｅｑｕｅｓｔ
    :param url:
    :param headers:
    :return:
    '''
    proxies = random.choice(proxies_list)
    res = requests.get(
                            url=url,
                            headers=headers,
                            proxies=proxies,
                            timeout=20
                        )
    res.encoding='utf8'
    return res.text

def add_Cart(ASIN,offerListingID):
    '''
    模拟添加购物车，进一步获取库存(从商品详情页进）
    :param ASIN:
    :return:
    '''

    add_Cart_url = 'https://www.amazon.com/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance'

    proxies = random.choice(proxies_list)
    headers = header_form_data_obj.USA_Add_cart_header()
    Form_data = header_form_data_obj.from_Data(ASIN=ASIN,offerListingID=offerListingID)
    for i in range(3):
        try:
            res = requests.post(
                                url=add_Cart_url,
                                headers=headers,
                                data=Form_data,
                                #proxies=proxies,
                                timeout = 20
                                )
            res.encoding = 'utf8'
            add_cart_responses = res.text
            break
        except Exception as e:
            logger.exception('add_Cart')
            add_cart_responses = 'N.A'
    return add_cart_responses

def into_Sellers_list(sellers_list_url):
    '''
    用于没有黄金购物车时（没有seller),进入sellers_list 页面，获取页面内容
    :param sellers_list_url:
    :return: sellers_list_responses
    '''
    headers = header_form_data_obj.USA_Sellers_list_Header()
    ## 调用前面封装好的自己的请求头（get)
    for i in range(2):
        try:
            sellers_list_responses = myrequest_get(url=sellers_list_url,headers=headers)
            break
        except Exception as e:
            logger.exception('into_Sellers_list')

    return sellers_list_responses

def sellers_list_add_Cart(ASIN,offeringID):
    add_Cart_url = 'https://www.amazon.com/gp/item-dispatch/ref=olp_atc_new_1'
    proxies = random.choice(proxies_list)
    headers = header_form_data_obj.USA_Sellers_list_addcart_Header()
    Form_data = header_form_data_obj.form_Data_03(ASIN,offeringID)
    res = requests.post(
                        url=add_Cart_url,
                        headers=headers,
                        data=Form_data,
                        proxies=proxies
                        )

    res.encoding='utf8'
    add_cart_responses = res.text
    return add_cart_responses

def updata_Shopping_nub(ASIN,offeringID):
    '''
    修改购物车里　对应商品的　购买数量　
    :param ASIN:
    :param offeringID:
    :return:
    '''
    updata_url = 'https://www.amazon.com/gp/cart/ajax-update.html/ref=ox_sc_update_quantity_1%7C100%7C999'
    headers = header_form_data_obj.USA_updata_Shopping_nub_Header()
    proxies = random.choice(proxies_list)
    form_data = header_form_data_obj.form_Data_02(ASIN=ASIN,offeringID=offeringID)
    res = requests.post(
                        url=updata_url,
                        headers=headers,
                        data=form_data,
                        proxies=proxies
                        )
    res.encoding='utf8'
    after_updata_responses = res.text
    return after_updata_responses




class UKUesToSencodAnalysis():

    def __init__(self):

        self.cookies = ['at-acbuk=Atza|IwEBILB65q8rA2KSv-Y8WFXWgH0UgGbtkWh138wiqt30gBmlJoFVqHF-RB_cziU8xf97HVVgoc7PHRJVcHvnz200wg5jUAdPozEskgo7DdZTgPMKSK-grfbbN3EZIGfcWEuok2g-diK2jy8OggRAt8k5ej_ZwR4MS6w1NDI0N25OaqU9gOq7WRak4khdNV1z7cSlOVR5vRDbIN4EoBlCzn3TfLROmwUYMOwp1OAWCxZniWqU3_UEjJgBLu-BF5awXhVmjWrh2VFm2Oeg87c40AZxIppx0T6hMB-Ap8OScBubGE0BtdG44RLbUZX7PMj-MiTd1i9qhqvybdatVFrGQaAM2BZMOpfYDntKyI2-otvFkqln7_Q1yqNsJ4zozlXL4oMTgMVpDybUm8TrHiiPdTrlZETX; sess-at-acbuk="Nuv2g/dTPhm4YjP6mh6hUAAm6VgZP3p/hJdAnRcadr0="; sst-acbuk=Sst1|PQGsOeWO2qEow4NwlQj1gOY5Cxj5QlTHhg-L3rcs9PAvIYbb710RcSF_p551DagxfFp0LHldbQQ0mJ04YTg8pEG_KurLjd05IWRE6LD1k2-2QfmsRPwWbhtfq7DLc-IZxVWSL2TE9a47-owVudIUUbUd3YQddFNoGkM1x4MDEOe3uOP06flbRZ-f416a7nh2WBb477ll2Otiy5wlU0nGTRktmiRh9WHfx5j_9T7XXTgKbARSiPFNniIWitk5dGNiDPz44McutLcLni1rgO-olN4krQoNsm_7rchji9lTG3AIJv9A_LRLQCbRadwgmbUj3_hJHepFXc-OP9NLnmYhCA1Kzw; x-wl-uid=1muHCEEwwEyWq0VHosiHEIhK+KteZZdxwOkO8RB4DzUorsFMkQxLiwMDY4bOkZPTcwezTMn0zV15TFgEPZEOkCg==; lc-acbuk=en_GB; session-token="HDO2XErJEEaH7lXXCpHmpW20KJxj7Lc4kCX8Rza8XNbNaheYZpjBLvzWe441Dahk62ldVDBKlkwXpt2fjovV2T+VXjdzdfmasz8qOEvpI/lBxH3q7zcGBBvXoUndwANqwjLfTkueRG7ytHbYCZhmZzg71bUmUwzLyjVpRhCdrwUFilD0iJvMoMvmp5jpZwLIFqf86iYySlhdjc0RtmdmnjSTPXgvIhQpENd/6q1upcsEaC0slDM81DgYHDgGdI003Cym6mv6ZWE9DycL66sK9w=="; x-acbuk="74P@bJpcWxl2tNk6mUvBXgxPaT8YlslXrwRwXIG5y3woZtzlLTWe1d33@w46RcCL"; ubid-acbuk=259-2948611-7840936; session-id-time=2082758401l; session-id=259-1136416-4224409; csm-hit=tb:6ECT33MTBP2AHACV54XZ+s-6ECT33MTBP2AHACV54XZ|1537452457609&adb:adblk_no&t:1537452457609']

        self.user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36']

        self.add_cart_url = 'https://www.amazon.co.uk/gp/product/handle-buy-box/ref=dp_start-bbf_1_glance'

    def UK_Add_Cart_Headers(self):
        '''
        构建详情页面加入购物车操作的请求头
        :return:
        '''
        cookie = random.choice(self.cookies)
        user_agent =random.choice(self.user_agents)
        headers = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding':'gzip, deflate',
            'accept-language':'zh-CN,zh;q=0.8',
            'cache-control':'max-age=0',
            'content-length':'598',
            'content-type':'application/x-www-form-urlencoded',
            'cookie':cookie,
            'origin':'https://www.amazon.co.uk',
            'upgrade-insecure-requests':'1',
            'user-agent':user_agent
        }
        return headers

    def UK_Into_Sellers_List_Headers(self):
        '''
        构建进入卖家列表页面的请求头
        :return:
        '''
        cookie = random.choice(self.user_agents)
        user_agent =random.choice(self.user_agents)

        headers = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, sdch',
            'accept-language':'zh-CN,zh;q=0.8',
            'cookie':cookie,
            'upgrade-insecure-requests':'1',
            'user-agent':user_agent
        }
        return headers

    def UK_Add_Cart_Form_Data(self,ASIN,offerListingID):
        '''
        添加购物车时使用ＰＯＳＴ参数
        :param ASIN:
        :param offerListingID:
        :return:
        '''

        form_data = {
            'session-id':'259-1136416-4224409',
            'ASIN':ASIN,
            'offerListingID':offerListingID,
            'isMerchantExclusive':'0',
            'merchantID':'ARKG530VO6V7A',
            'isAddon':'0',
            'nodeID':'328228011',
            'sellingCustomerID':'ARKG530VO6V7A',
            'tagActionCode':'328228011',
            'viewID':'glance',
            'rsid':'259-1136416-4224409',
            'quantity':9999999,
            'submit.add-to-cart':'Add to Basket',
            'dropdown-selection':'add-new',
            'dropdown-selection-ubb':'add-new'
        }
        return form_data

    def UK_Add_Cart(self,ASIN,offerListingID):
        '''
        加入购物车，并获取返回的内容
        :param ASIN:
        :param offerListingID:
        :return:
        '''
        headers = self.UK_Add_Cart_Headers()
        form_data = self.UK_Add_Cart_Form_Data(ASIN=ASIN,offerListingID=offerListingID)
        url = self.add_cart_url
        res = requests.post(
                                url=url,
                                headers=headers,
                                data = form_data
                            )
        res.encoding='utf8'
        responses = res.text

        return responses

    def UK_Into_sellers_list(self,into_sellers_list_url):
        '''
        获取卖家列表页面
        :param into_sellers_list_url:
        :return:
        '''
        headers = self.UK_Into_Sellers_List_Headers()
        res = requests.get(
                                url=into_sellers_list_url,
                                headers = headers
                            )
        res.encoding='utf8'
        responses = res.text
        return  responses



uk_use_to_sencond_analysis = UKUesToSencodAnalysis()





if __name__ == "__main__":
    show_responses_html(add_Cart('6040791616',''))
    # show_responses_html(updata_Shopping_nub('B004MYDX5E'))
    # show_responses_html(into_Sellers_list(sellers_list_url='https://www.amazon.com/gp/offer-listing/B00D1SZNO6/ref=dp_olp_new_mbc?ie=UTF8&condition=new'))
    # show_responses_html(sellers_list_add_Cart('ASIN', 'offeringID'))
    # show_responses_html(updata_Shopping_nub('B00D1SZNO6',offeringID='o5TTa0aDranmH%2Bm4XnPo5N%2F%2F7I3vUeTmHNNXmrdhvd730DICATO5kUwpxmICDDBaHcicOY0ws1tSTBd%2B7S7C%2FHxaJdvT%2B0aB6RiBh2N47euTOd8JoDkN4f37TIRDKa8q7MAeagBoUyd4k%2F9pDd0dgC6%2BxQGF6zu1'))
    # show_responses_html(uk_use_to_sencond_analysis.UK_Add_Cart(ASIN='B01LNFWNQY',offerListingID='qUnRNHUUlx0lozUeDld5JWOYnYj2XnHNKnRxn4lKZ9hRiPBn8Y3BodWDqGkSvJUGf80SklfDD6ES0pXdc2NiUjxqqM3gW0YLo1WcGbb9nAE%3D'))
    show_responses_html(add_Cart(ASIN='B00763LZWQ',offerListingID='QVKqHh1XPEeaxGSTZoRhztAW4fWbWR17hJB6s0aELagbV52wxu6xgfnRQnnEC4tTIc2eB6q6Xk0Eg%2BIKNbCdE41ekzCASWNzL%2FN5amOgsW8D99n6WPOZAQ%3D%3D'))
    pass

