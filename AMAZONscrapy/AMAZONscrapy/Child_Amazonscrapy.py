import requests

from AMA_ANALYSIS.USA_analysis import create_USA_analysis_obj

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


def send_Request(url, proxies='null'):
    '''
    发起请求，获取返回内容
    in:     url,headers,user-agent,proxies
    out:    responses
    '''
    if proxies == 'null':
        res = requests.get(url=url, headers=headers, timeout=5)
    else:
        res = requests.get(url=url, headers=headers, proxies=proxies, timeout=5)
    res.encoding = 'utf8'
    responses = res.text
    request_url = res.url
    response_status_code = res.status_code
    # show_Get(responses)
    return responses, request_url, response_status_code


def get_keyWord(responses, request_url):
    '''
    获取产品介绍并做分词处理
    :param responses:
    :param request_url:
    :return:
    '''
    product_introduction = create_USA_analysis_obj(all_response=responses, url=request_url).get_Product_Introduction()
    return product_introduction

def run_child_scrapy(url):
    '''
    子爬虫的控制逻辑
    :param url:
    :return:
    '''
    responses, request_url = send_Request(url=url)
    product_introduction = get_keyWord(responses, request_url)
    return product_introduction

