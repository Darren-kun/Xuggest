


class CONSTRUCTURL():

    def counstruct_USA_url(self,ASIN):
        '''
        将ASIN 构建成美国　ｕｒｌ
        :param ASIN:
        :return url:
        '''
        url = 'https://www.amazon.com/dp/' + ASIN
        return url

    def counstruct_UK_url(self,ASIN):
        '''
        将ASIN 构建成英国　ｕｒｌ
        :param ASIN:
        :return:
        '''
        url = 'https://www.amazon.co.uk/dp/' + ASIN
        return url

def counstruct_Url(ASIN,country):
    '''
    判断国家，构建不同国家的ｕｒｌ
    :param ASIN:
    :param country:
    :return url:
    '''
    counstruct_obj = CONSTRUCTURL()
    url = ''
    print(country)
    if country == 'com':
        print('into com')
        if ASIN:
            url = counstruct_obj.counstruct_USA_url(ASIN=ASIN)
        pass

    elif country == 'co.uk':
        if ASIN:
            url = counstruct_obj.counstruct_UK_url(ASIN=ASIN)

    return url