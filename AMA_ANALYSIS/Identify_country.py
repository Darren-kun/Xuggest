import re


def identify_Country(url):
    '''
    根据ｕｒｌ　判断国家
    :param url:
    :return:
    '''
    country_re_list = [
        'amazon.([\s\S]*?)/'
    ]

    for re_exp in country_re_list:
        country_result_list = re.findall(re_exp, url)
        if len(country_result_list) >= 1:
            Country = country_result_list[0]

            break

    if Country == 'com':
        return 'USA'

    elif Country == 'de':
        return 'DE'

    elif Country == 'co.uk':
        return 'UK'