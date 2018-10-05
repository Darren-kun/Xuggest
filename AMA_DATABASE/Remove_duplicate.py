import re

remove_Duplicate_list = []
class REMOVE():

    def remove_Duplicate_ASIN_url(self,url):
        '''
        去掉重复的ＡＳＩＮ　ｕｒｌ
        :param url: 
        :return: 
        '''

        ASIN_re_list = [
            '/([A-Z0-9]+)/',
            '/(B[\s\S]*?)$'
        ]
        if len(remove_Duplicate_list)>40000:
            remove_Duplicate_list[:] = remove_Duplicate_list[30000:]

        for re_exp in ASIN_re_list:
            ASIN_result_list = re.findall(re_exp,url)
            if ASIN_result_list:
                ASIN = ASIN_result_list[0]
                break
        if ASIN:
            if ASIN in remove_Duplicate_list:
                return 0,0
            else:
                remove_Duplicate_list.append(ASIN)
                return url,ASIN
        else:
            return True,True

remove_obj = REMOVE()