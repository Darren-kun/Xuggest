import redis

try:
    from AMAZONscrapy.AMAZONscrapy.settings import submit_key
except Exception as e:
    #scrapy运行时使用
    from AMAZONscrapy.settings import submit_key


class MYREDIS():
    '''
    提供ｓｃｒａｐｙ使用打扩展功能模块
    '''
    def submit_Product_info(self,redis_obj,product_info):
        '''
        往远程数传输数据
        :param redis_obj:
        :param submit_key:
        :param product_info:
        :return:
        '''
        for i in range(3):
            try:
                redis_obj.rpush(submit_key,product_info)
                break
            except Exception as e:
                print(e)
                continue


    def add_Url(self,redis_obj,submit_key,Recommend_product_url_list):
        '''
        添加获取下来的ｕｒｌ
        :param redis_obj:
        :param submit_key:
        :param product_info:
        :return:
        '''
        if Recommend_product_url_list:
            for one_Recommend_product_url in Recommend_product_url_list:
                if one_Recommend_product_url:
                    try:
                        product_url = one_Recommend_product_url[0]
                        redis_obj.rpush(submit_key,product_url)
                    except Exception as e:
                        print(e)
                else:
                    pass
        else:
            return False

    def add_top100_Url(self,redis_obj,submit_key,Recommend_product_url_list):
        '''
        添加获取下来的ｕｒｌ
        :param redis_obj:
        :param submit_key:
        :param product_info:
        :return:
        '''
        if Recommend_product_url_list:
            for one_Recommend_product_url in Recommend_product_url_list:
                if one_Recommend_product_url:
                    try:
                        product_url = one_Recommend_product_url
                        redis_obj.rpush(submit_key,product_url)
                    except Exception as e:
                        print(e)
                else:
                    pass
        else:
            return False



myredis_obj = MYREDIS()