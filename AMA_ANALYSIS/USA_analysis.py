# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:13:07 2018

@author: PC1
"""

# -*- coding: utf-8 -*-
from ama_blog import logger

"""
Created on Wed Aug 29 14:39:51 2018

@author: Darren_KUN
"""

import re
from lxml import etree
from AMA_ANALYSIS.analysis_request_header import add_Cart,into_Sellers_list
from AMA_ANALYSIS_TEST.show_respones_html import show_responses_html
import signal

class USAgetinfo():
    '''
    获取商品详情页面上的信息（USA）
    获取的信息有：picture，brand，title，Rating，Reviews，price，stock，seller，Sellers，Dimensions，Weigth，ranking,Category
    每个方法获取一个数据

    '''

    def __init__(self, all_response, product_url):
        self.response = all_response
        self.etree_html = etree.HTML(all_response)
        self.product_url = product_url

    ##用于辅助　获取商品信息
    def get_Sellers_url(self):
        '''
        获取进入卖家列表的ｕｒｌ
        :return:
        '''

        Sellers_url_xpath_list = [
                                    '//*[@id="olp_feature_div"]/div/span[1]/a/@href',

                                ]

        Sellers_url_re_list = [
                                    '''class="a-size-small aok-float-right a-center"><a href="([\s\S]*?)"''',
                                    'a href="[\s\S]*?"><b>New</b> \((\d.*)\) ',
                                    '\(\d+\) ',
                                ]


        ASIN, Country = self.get_ASIN_country()
        Sellers_url_header = 'https://www.amazon.' + Country
        for xpath in Sellers_url_xpath_list:
            Seller_url_result_list = self.etree_html.xpath(xpath)
            if len(Seller_url_result_list) == 1:
                sellers_list_url = Sellers_url_header + Seller_url_result_list[0]
                break
            else:
                sellers_list_url = 'N.A'

        if sellers_list_url == 'N.A':
            print('into seller re')
            # show_responses_html(self.response)
            for re_exp in Sellers_url_re_list:
                Seller_url_result_list = re.findall(re_exp,self.response)
                print(Seller_url_result_list)
                if Seller_url_result_list:
                    sellers_list_url = Sellers_url_header + Seller_url_result_list[0]
                    break

        if sellers_list_url == 'N.A':
            sellers_list_url = Sellers_url_header +  '/gp/offer-listing/' + ASIN + '/ref=dp_olp_all_mbc?ie=UTF8&condition=all'

        return sellers_list_url

    def get_offerListingID(self):

        offerlistID_re_list = [
            'offerListingID" value="([\s\S]*?)"'
        ]

        for re_exp in offerlistID_re_list:
            offerlistID_result_list = re.findall(re_exp,self.response)
            print('offerlistID_result_list',offerlistID_result_list)
            if len(offerlistID_result_list) >= 1:
                offerListingID = offerlistID_result_list[0]

            else:
                offerListingID = ''

        return offerListingID

    ##上面的函数　用于辅助准确的获取商品信息
    ##下面函数为　需要获取的商品信息

    def get_Picture_url(self):
        '''
        获取图片，图片用 ASIN 命名
        '''
        Picture_url_re_list = [
                                'var encodedImgSrc = "([\s\S]*?)"; ',
                                'var encodedImgSrc = "([\s\S]*?)"'
                            ]

        for re_exp in Picture_url_re_list:
            Picture_result_list = re.findall(re_exp, self.response)
            if len(Picture_result_list) == 1:
                Picture_url = Picture_result_list[0]
            else:
                Picture_url = ''

        return Picture_url

    def get_Brand(self):
        '''
        获取品牌名
        '''
        Brand_xpath_list = [
                                '//*[@id="bylineInfo"]/text()',
                            ]

        Brand_src_xpath_list = [
                                    '//*[@id="brand"]/@src'
                                ]

        Brand_re_list = [
                            '''<a id="bylineInfo" class="[\s\S]*?">([\s\S]*?)</a>'''
                        ]

        Brand = 'N.A'
        for xpath in Brand_xpath_list:
            Brand_result_list = self.etree_html.xpath(xpath)
            if len(Brand_result_list) == 1:
                Brand = Brand_result_list[0]
                break



        if Brand == 'N.A':
            for re_exp in Brand_re_list:
                Brand_result_list = re.findall(re_exp, self.response)

                if len(Brand_result_list) == 1:
                    Brand = Brand_result_list[0]

        if Brand == 'N.A':
            for xpath in Brand_src_xpath_list:
                Brand_result_list = self.etree_html.xpath(xpath)
                if len(Brand_result_list) == 1:
                    Brand = Brand_result_list[0]
                    break

        return Brand

    def get_Title(self):
        '''
        获取标题
        '''
        Title_xpath_list = [
                                '//*[@id="productTitle"]/text()'
                            ]

        Title = 'N.A'
        for xpath in Title_xpath_list:
            Title_result_list = self.etree_html.xpath(xpath)
            if len(Title_result_list) == 1:
                Title = Title_result_list[0].replace('\n', '').replace('  ', '')
                break

        return Title

    def get_Rating(self):
        '''
        获取评级，星
        '''
        Rating_xpath_list = [
                                '//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()'
                            ]

        Rating_re_list = [
                                '<span class="a-icon-alt">((\d|\d.\d) out of (\d|\d.\d) stars)</span>'
                            ]

        get_end_number_re_list = [
                                    '(\d|\d.\d) out of'
                                ]

        Rating = 'N.A'
        for xpath in Rating_xpath_list:
            Rating_result_list = self.etree_html.xpath(xpath)
            if len(Rating_result_list) == 1:
                Rating = Rating_result_list[0]
                break

        if Rating == 'N.A':
            for re_exp in Rating_re_list:
                Rating_result_list = re.findall(re_exp, self.response)
                if len(Rating_result_list) > 0:
                    Rating = Rating_result_list[0][0]

        if Rating != 'N.A':
            for re_exp in get_end_number_re_list:
                try:
                    Rating = float(re.findall(re_exp,Rating)[0])
                except Exception as e:
                    Rating = -4

        else:
            Rating = -1

        return Rating

    def get_Reviews(self):
        '''
        获取评价量
        '''
        Reviews_xpath_list = [
                                '//*[@id="acrCustomerReviewText"]/text()',
                                '//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()'
                            ]

        Reviews_re_list = [
                            '<span id="acrCustomerReviewText" class="a-size-base">(\d.*?[\s\S]*?)</span>'
                        ]

        get_end_number_re_list = [
                                    '\d+',
                                    '([\s\S]*?) customer reviews'
                                ]

        Reviews = 'N.A'

        for xpath in Reviews_xpath_list:
            Reviews_result_list = self.etree_html.xpath(xpath)

            if len(Reviews_result_list) == 1:
                Reviews = Reviews_result_list[0].replace(',','')
                break

        if Reviews == 'N.A':
            for re_exp in Reviews_re_list:
                Reviews_result_list = re.findall(re_exp, self.response)
                print('Reviews_result_list',Reviews_result_list)
                if len(Reviews_result_list) > 0:
                    Reviews = Reviews_result_list[0].replace(',','')
                else:
                    Reviews = 0

        if Reviews != 'N.A' and Reviews != 0:
            print('Reviews',Reviews)
            for re_exp in get_end_number_re_list:
                try:
                    Reviews = re.findall(re_exp, Reviews)[0].replace(',','')
                    break
                except Exception as e:
                    Reviews = '-4'

        Reviews = int(Reviews)
        return Reviews

    def get_Answered(self):

        Answered_xpath_list = [
            '//*[@id="askATFLink"]/span/text()',
        ]

        get_end_number_re_list = [
                                    '\d+',
                                ]

        Answered = -1
        for xpath in Answered_xpath_list:
            Answered_result_list = self.etree_html.xpath(xpath)

            if len(Answered_result_list) == 1:
                try:
                    Answered = Answered_result_list[0].replace(',','')
                    break
                except Exception as e:
                    pass


        if Answered != -1:
            try:
                Answered = re.findall('\d+',Answered)[0]
            except Exception as e:
                Answered = -4

        return Answered

    def get_Price(self):
        '''
        获取价格
        '''
        Price_xpath_list = [
                                '//*[@id="priceblock_dealprice"]/text()',
                                '//*[@id="priceblock_ourprice"]/text()',
                                '//*[@id="price_inside_buybox"]/text()',
                                '//*[@id="buyNewSection"]/a/h5/div/div[2]/div/span[2]/text()'
                            ]

        Price_re_list = [
                            '''id="price_inside_buybox" class="a-size-medium a-color-price">([\s\S]*?)<'''
                        ]

        Price = -1
        for xpath in Price_xpath_list:
            Price_result_list = self.etree_html.xpath(xpath)
            if len(Price_result_list) == 1:
                Price = Price_result_list[0][1:].replace('$','').replace(' ','').replace('\n','').replace(',','')
                if '-' in Price:
                    Price = -1
                break

        if Price == -1:
            for re_exp in Price_re_list:
                Price_result_list = re.findall(re_exp, self.response)

                if len(Price_result_list) == 1:
                    Price = Price_result_list[0].replace(' ', '').replace('\n', '').replace('$','').replace(',','')
                    if '-' in Price:
                        Price = -1
                    break
        Price = float(Price)
        return Price

    def get_Stock(self):
        '''
        获取库存
        '''
        Stock_xpath_list = [
                                '//*[@id="availability"]/span/text()',
                                '//*[@id="availability"]/text()',
                                '//*[@id="outOfStock"]/div/span/text()',
                            ]

        Stock_re_list = [
                            'class="a-size-medium a-color-success">([\s\S]*?)<',
                            'class="a-size-medium a-color-state">\s*([\s\S]*?)\s*</span'
                        ]

        Stock = 'N.A'
        for xpath in Stock_xpath_list:
            Stock_result_list = self.etree_html.xpath(xpath)
            print('Stock_result_list:',Stock_result_list)
            if len(Stock_result_list) == 1:
                Stock = Stock_result_list[0].replace('\n', '').replace('  ', '')
                if len(Stock)>4:
                    break

        print('Stock:', Stock)
        if Stock == 'N.A' or Stock == '':
            for re_exp in Stock_re_list:
                Stock_result_list = re.findall(re_exp, self.response)
                print('Stock_result_list:', Stock_result_list)
                if len(Stock_result_list) >= 1:
                    Stock = Stock_result_list[0].replace('\n', '').replace('  ', '')
                    break

        if Stock == 'N.A' or Stock == '':
            Stock = 'In Stock.'

        print('Stock:',Stock)
        return Stock

    def get_Seller(self):
        '''
        获取卖家
        '''
        Seller_xpath_list = [
                                '//*[@id="merchant-info"]/text()',
                                '//*[@id="SSOFpopoverLink"]/text()',
                                '//*[@id="merchant-info"]/a/text()',
                            ]

        Seller_re_list = [
                            '''id="merchant-info" class="a-section a-spacing-mini">\s*?[\s\S]*?by([\s\S]*?)<span''',
                            '''Sold by <a href='[\s\S]*?'>([\s\S]*?)</a>''',
                            '''sold by <a href='[\s\S]*?'>([\s\S]*?)</a>'''
                            '''Ships from and sold by <a href='[\s\S]*?'>([\s\S]*?)</a>''',
                            '''Ships from and sold by([\s\S]*?)\.'''
                        ]

        Seller = 'N.A'
        for xpath in Seller_xpath_list:
            Seller_result_list = self.etree_html.xpath(xpath)
            print('Seller_result_list:',Seller_result_list)
            if len(Seller_result_list) == 1:
                Seller = Seller_result_list[0].replace('\n', '').replace('  ', '').replace('.com.','')
                if 0< len(Seller) < 100 :
                    break


        if Seller == 'N.A' or Seller =='Fulfilled by Amazon':
            for re_exp in Seller_re_list:
                Seler_result_list = re.findall(re_exp, self.response)
                if len(Seler_result_list) >= 1:
                    Seller = Seler_result_list[0].replace('\n', '').replace('  ', '').replace('.com.','')
                    if len(Seller) > 50:
                        Seller = 'N.A'
                    elif '<' in Seller and '/' in Seller:
                        Seller = 'N.A'

                    else:
                        break


        return Seller

    def get_Sellers(self):
        '''
        获取卖家数量
        '''
        Sellers_xpath_list = [
                                '//*[@id="olp_feature_div"]/div/span[1]/a/text()',
                                '//*[@id="mbc"]/div[1]/div/h5[1]/span/a/text()',
                                '//*[@id="unqualified"]/div[1]/a/text()'
                            ]

        get_end_number_re_list = [
                                '\((\d+)\)',
                                '\d*'
                            ]

        Sellers = -1
        for xpath in Sellers_xpath_list:
            Sellers_result_list = self.etree_html.xpath(xpath)
            if len(Sellers_result_list) == 1:
                Sellers = Sellers_result_list[0]
                print('Sellers:',Sellers)
                break

        if Sellers != -1:
            for re_exp in get_end_number_re_list:
                try:
                    Sellers = int(re.findall(re_exp,Sellers)[0])
                    break
                except IndexError as e:
                    pass


        return Sellers

    def get_Dimensions(self):
        '''
        获取尺寸
        '''
        Dimensions_xpath_list = [
                                    '//*[@id="variation_size_name"]/div/span[1]/text()',
                                    '//*[@id="detailBullets_feature_div"]/ul/li[1]/span/span[2]/text()',
                                    '//*[@id="tech-specs-table-left"]/tbody/tr[1]/td[2]/p//text',
                                ]

        Dimensions_re_list = [
            '''  Product Dimensions: 
            </b>
            ([\s\S]*?)
            </li>''',
            '\s*Product Dimensions\n\s*?</th>\n\s*\n\s*\n\s*\n\s*\n\s*?\n\s*?<td class="a-size-base">\n\s*?(\d[\s\S]*?)\n\s*?</td>',
            '''<td class="a-size-base">([\s\S]*?)</td>''',
            '<td class="a-size-base">\s*?(\d.*?\.\d x[\s\S]*?)<',
            'Size:(\d[\s\S]*?)<',
            '''Product Dimensions: \n\s*</b>\n\s*([\s\S]*?)\n\s*</li>''',
            'Package Dimensions\n\s*</th>\n\s*\n\s*\n\s*\n\s*\n\s*\n\s*<td class="a-size-base">\n\s*(\d[\s\S]*?)\s*\n\s*</td>'
        ]

        Dimensions = 'N.A'
        for re_exp in Dimensions_re_list:
            Dimensions_result_list = re.findall(re_exp, self.response)
            print('Dimensions_result_list',Dimensions_result_list)
            if len(Dimensions_result_list) == 1:

                Dimensions = Dimensions_result_list[0].replace(' ', '').replace('\n', '')
                if len(Dimensions) < 30:
                    break
                else:
                    Dimensions = '-1'

            elif len(Dimensions_result_list) > 1:

                for Dimensions_result in Dimensions_result_list:
                    Dimensions_result = Dimensions_result.replace(' ', '').replace('\n', '')
                    if 'x' in Dimensions_result and len(Dimensions_result) < 40:
                        Dimensions = Dimensions_result
                        if len(Dimensions):
                            break


        if Dimensions == 'N.A':
            for xpath in Dimensions_xpath_list:
                Dimensions_result_list = self.etree_html.xpath(xpath)
                if len(Dimensions_result_list) == 1:
                    Dimensions = Dimensions_result_list[0].replace('\n', '').replace('  ', '')
                    break
        return Dimensions

    def get_Size(self):
        '''
        获取　尺码（跟尺寸不同）
        :return:
        '''
        Size = '-1'
        Size_xpath_list = [
                                '//*[@id="dropdown_selected_size_name"]/span/span/span/text()',
                                '//*[@id="variation_size_name"]/div/span/text()'
                            ]

        for xpath in Size_xpath_list:
            Size_result_list = self.etree_html.xpath(xpath)
            if Size_result_list:
                try:
                    Size = Size_result_list[0].replace('  ','').replace('\n','')
                    break
                except Exception as e:
                    Size = '-1'
                    break
        return Size

    def get_ASIN_country(self):
        '''
        获取ASIN
        '''
        ASIN_xpath_list = [
                                '//*[@id="detail-bullets"]/table/tbody/tr/td/div[2]/ul/li[5]/text()',
                                '//*[@id="mbc"]/div/div/h5[1]/span/a/text()'
                            ]

        ASIN_re_list_01 = [
                            'ASIN:\n\s*</span>\n\s*[\s\S]*?>([A-Z0-9]*)</span>',
                            'ASIN:</b>\s*([0-9A-Z]*?)\s*</li>'
                        ]

        ASIN_re_list_02 = [
                            '/([A-Z0-9]+)/',
                            '/([0-9A-Z]+)$'
                        ]


        country_re_list = [
                                'amazon.([\s\S]*?)/'
                            ]

        ASIN = 'N.A'

        for re_exp in ASIN_re_list_01:
            ASIN_result_list = re.findall(re_exp, self.response)
            if len(ASIN_result_list) == 1:
                ASIN = ASIN_result_list[0]
                break

        if ASIN == 'N.A':
            for re_exp in ASIN_re_list_02:
                ASIN_result_list = re.findall(re_exp, self.product_url)
                if len(ASIN_result_list) == 1:
                    ASIN = ASIN_result_list[0]
                    break
            

        if ASIN == 'N.A':
            for xpath in ASIN_xpath_list:
                ASIN_result_list = self.etree_html.xpath(xpath)
                if len(ASIN_result_list) == 1:
                    ASIN = ASIN_result_list[0].replace('\n', '').replace('  ', '')
                    break

        for re_exp in country_re_list:
            country_result_list = re.findall(re_exp, self.product_url)
            if len(ASIN_result_list) == 1:
                Country = country_result_list[0]
                break
            Country = 'N.A'

        return ASIN, Country

    def get_Weigth(self):
        '''
        获取重量
        '''
        Weigth_xpath_list = [
                                '//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[2]/td/text()',

                            ]

        Weigth_re_list = [
                                'Shipping Weight[\s\S]*?(\d[\s\S]*?)(\(|<)',
                                'Shipping Weight[\s\S]*?(\d[\s\S]*?)\(',
                                'Shipping Weight:</b> ([\s\S]*?[a-z])',
                                '<td class="a-size-base">([\s\S]*?)</td>'
                            ]

        for re_exp in Weigth_re_list:
            Weigth_result_list = re.findall(re_exp, self.response)
            print('Weigth_result_list',Weigth_result_list)
            if len(Weigth_result_list) == 1:
                Weigth = Weigth_result_list[0][0].replace('\n','').replace('  ','')
                break

            elif len(Weigth_result_list) > 1:

                for Weigth_result in Weigth_result_list:
                    Weigth_list = re.findall('^\d', Weigth_result[0].replace('\n', '').replace('  ', ''))
                    if len(Weigth_list) > 0 and 'x' not in Weigth_result:
                        Weigth = Weigth_result[0].replace('\n', '').replace('  ', '')
                        break
                break

            else:
                Weigth = 'N.A'

        if Weigth == 'N.A':
            for xpath in Weigth_xpath_list:
                Weigth_result_list = self.etree_html.xpath(xpath)
                if len(Weigth_result_list) == 1:
                    Weigth = Weigth_result_list[0].replace('\n','').replace(' ','')
                    break
        return Weigth
    #
    # def get_Ranking(self):
    #     '''
    #     获取排名
    #     '''
    #     Ranking_xpath_list = [
    #         '//*[@id="SalesRank"]/ul/li[1]/span[1]/text()'
    #     ]
    #     Ranking_re_list = [
    #         '(#\d*|#\d*,\d*) in <'
    #     ]
    #     Ranking = 'N.A'
    #     for xpath in Ranking_xpath_list:
    #         Ranking_result_list = self.etree_html.xpath(xpath)
    #         if len(Ranking_result_list) == 1:
    #             Ranking = int(Ranking_result_list[0][1:].replace(',',''))
    #             break
    #
    #
    #     if Ranking == 'N.A':
    #         for re_exp in Ranking_re_list:
    #             Ranking_result_list = re.findall(re_exp, self.response)
    #             if len(Ranking_result_list) > 0:
    #                 Ranking = int(Ranking_result_list[0][1:].replace(',',''))
    #             else:
    #                 Ranking = -1
    #
    #     return Ranking

    # def get_Category(self):
    #     '''
    #     获取分类
    #     '''
    #     Category_xpath_list = [
    #                                 '//*[@id="SalesRank"]/ul/li[1]/span[2]/a[1]/text()'
    #                             ]
    #
    #     Category_re_list = [
    #                             'href="[\s\S]*?">([A-Z][a-z]*? &[\s\S]*?)<'
    #                         ]
    #
    #     for xpath in Category_xpath_list:
    #         Category_result_list = self.etree_html.xpath(xpath)
    #
    #         if len(Category_result_list) == 1:
    #             Category = Category_result_list[0]
    #             break
    #         Category = 'N.A'
    #
    #     if Category == 'N.A':
    #         for re_exp in Category_re_list:
    #             Category_result_list = re.findall(re_exp, self.response)
    #             if len(Category_result_list) > 0:
    #                 Category = Category_result_list[0]
    #
    #     return Category

    def get_s_Ranking_Category(self):
        '''
        获取全部的　排名对应的小分类
        :return:
        '''
        s_Ranking_Category_xpath_list = [
            '''//*[@id="SalesRank"]/ul//text()''',
            '''//*[@id="SalesRank"]/td[2]/ul//text()''',
            '''//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[6]/td/span/span/text()'''
        ]

        s_Ranking_re_list = [
            '''#\d*,\d*|#\d+'''
        ]

        s_Category_re_list = [
            '''([A-Z][\s\S]*?[a-z])\\n'''
        ]

        s_Ranking_Category_list = []
        for xpath in s_Ranking_Category_xpath_list:

            s_Ranking_Category_result_list = self.etree_html.xpath(xpath)
            print('s_Ranking_Category_result_list:',s_Ranking_Category_result_list)
            if len(s_Ranking_Category_result_list)>3:
                s_Ranking_Category_result_str = ''.join(s_Ranking_Category_result_list)
                for re_exp in s_Category_re_list:
                    s_Category_list = re.findall(re_exp,s_Ranking_Category_result_str)
                for re_exp in s_Ranking_re_list:
                    s_Ranking_list = re.findall(re_exp,s_Ranking_Category_result_str)
                print('s_Category_list',s_Category_list,'\n','s_Ranking_list',s_Ranking_list)
                if len(s_Category_list) == len(s_Ranking_list):
                    for s_Ranking_Category_tuple in zip(s_Ranking_list,s_Category_list):
                        s_Ranking_Category_list.append(s_Ranking_Category_tuple)
                    break

        s_Ranking_Category_list_to = []
        print('s_Ranking_Category_list',s_Ranking_Category_list)
        for s_Ranking_Category in s_Ranking_Category_list:
            s_Ranking_Category_dict = {}
            print ('s_Ranking_Category',s_Ranking_Category)
            try:
                s_Ranking_Category_dict['s_Ranking'] = s_Ranking_Category[0]
                s_Ranking_Category_dict['s_Category'] = s_Ranking_Category[1]
                s_Ranking_Category_list_to.append(s_Ranking_Category_dict)
            except IndexError as e:
                pass
        s_Ranking_Category_list = s_Ranking_Category_list_to
        return s_Ranking_Category_list

    def get_big_Ranking_Category(self):
        '''
        获取　大分类类　及　对应的　排名
        :return:
        '''
        big_Ranking_Category_xpath_list = [
                                                '//*[@id="SalesRank"]/text()'
                                            ]

        big_Ranking_Category_re_list = [
                                            'Rank:[\s\S]*?#([\s\S]*?)in\s*([\s\S]*?)\(',
                                            '<span>#([\s\S]*?)\s*in\s*([\s\S]*?) \('
                                        ]

        big_Ranking = -1
        big_Category = 'N.A'
        for re_exp in big_Ranking_Category_re_list:
            big_Ranking_Category_reuslt_list = re.findall(re_exp,self.response)
            print('big_Ranking_Category_reuslt_list',len(big_Ranking_Category_reuslt_list))
            if big_Ranking_Category_reuslt_list:
                try:
                    big_Ranking = int(re.findall('\d+',big_Ranking_Category_reuslt_list[0][0].replace(' ','').replace('\n','').replace(',',''))[0])
                except Exception as e:
                    print(e)
                    big_Ranking = -4

                try:
                    big_Category = big_Ranking_Category_reuslt_list[0][1].replace('  ','').replace('\n','')
                    print('big_Category',big_Category)
                    if len(big_Category)>40:
                        big_Category = '-1'
                    break
                except Exception as e:
                    print(e)
                    big_Category = '-4'
                    break

        return big_Ranking,big_Category

    def get_Recommend_product_url(self):
        '''
        获取产品的推荐产品　图片ｕｒｌ和产品ｕｒｌ
        返回的内容　是列表　[(product_url,product_picture_url),(),..]
        :return:Recommend_product_list
        '''

        Recommend_product_re_list = [
                                        '<a class="a-link-normal" target="_top" rel="noopener" title="[\s\S]*?" href="([\s\S]*?)"[\s\S]*?src="([\s\S]*?)"',
                                        # '<a class="a-link-normal" href="([\s\S]*?)"[\s\S]*?src="([\s\S]*?)"'
                                    ]

        Recommend_product_xpath_list = []

        for re_exp in Recommend_product_re_list:
            Recommend_product_list = re.findall(re_exp, self.response)

        return Recommend_product_list

    def get_Ship(self):
        '''
        判断　发货方式
        :return:
        '''
        FBA_re_list = [
                            '''Sold by <a href='[\s\S]*?'>([\s\S]*?)</a>''',
                            '''Ships from and sold by Amazon'''
                        ]

        FBM_re_list = [
                            '''Ships from and sold by <a href='[\s\S]*?'>([\s\S]*?)</a>'''
                        ]

        Ship = 'N.A'
        for re_exp in FBA_re_list:
            FBA_result = re.findall(re_exp, self.response)
            print('FBA_result',FBA_result)
            if len(FBA_result) == 1:
                break

        for re_exp in FBM_re_list:
            FBM_result = re.findall(re_exp, self.response)
            print('FBM_result',FBM_result)
            if FBM_result:
                break

        if FBA_result:
            if not FBM_result:
                Ship = 'FBA'



        if FBM_result:
            Ship = 'FBM'

        print(Ship)
        return Ship

    ##获取衣服的颜色
    def get_Product_Color(self):
        '''
        获取衣服的颜色
        :return:
        '''
        Product_Color_xparh_list = [
                                        '//*[@id="variation_color_name"]/div/span/text()',
                                        '//*[@id="shelf-label-color_name"]/div/span/span/text()',
                                        '//*[@id="shelf-label-flavor_name"]/div/span/span/text()'
                                    ]

        for xpath in Product_Color_xparh_list:
            Product_Color_result_list = self.etree_html.xpath(xpath)

            if Product_Color_result_list:
                Product_Color = Product_Color_result_list[0].replace('\n','').replace('  ','')

            else:
                Product_Color = []

        return str(Product_Color)

    def get_Link_ASIN(self):

        Link_Color_ASIN_xpath = [
                                '//*[@id="variation_color_name"]/ul//@data-defaultasin',
                                '//*[@id="shelfSwatchSection-flavor_name"]//@data-dp-url'
                                 ]

        Link_Size_ASIN_xpath = [
                                '//*[@id="native_dropdown_selected_size_name"]//@value',
                                '//*[@id="variation_size_name"]/ul//@data-defaultasin',
                                '//*[@id="native_size_name_0"]//@value'
                                ]

        Link_ASIN_dict = {}
        for xpath in Link_Color_ASIN_xpath:
            Link_Color_ASIN_result_list = self.etree_html.xpath(xpath)
            print('Link_Color_ASIN_result_list:',Link_Color_ASIN_result_list)
            if Link_Color_ASIN_result_list:
                Link_Color_ASIN_list= []
                for Link_Color_ASIN in Link_Color_ASIN_result_list:
                    if 0 < len(Link_Color_ASIN) < 15:
                        Link_Color_ASIN_list.append(Link_Color_ASIN)
                    else:
                        try:
                            Link_Color_ASIN_list.append(re.findall('/dp/([\s\S]*?)/',Link_Color_ASIN)[0])
                        except Exception as e:
                            print(e)
                            pass

                Link_ASIN_dict['Link_Color_ASIN_list'] = Link_Color_ASIN_list
                break
            else:
                Link_ASIN_dict['Link_Color_ASIN_list'] = []

        for xpath in Link_Size_ASIN_xpath:
            Link_Size_ASIN_result_list = self.etree_html.xpath(xpath)
            Link_Size_ASIN_list =[]
            if Link_Size_ASIN_result_list:
                for Link_Size_ASIN in Link_Size_ASIN_result_list:
                    if Link_Size_ASIN:
                        if ',' in Link_Size_ASIN:
                            Link_Size_ASIN_list.append(Link_Size_ASIN[2:])
                        else:
                            Link_Size_ASIN_list.append(Link_Size_ASIN)
                Link_ASIN_dict['Link_Size_ASIN_list'] = Link_Size_ASIN_list
                break
            else:
                Link_ASIN_dict['Link_Size_ASIN_list'] = []


        return Link_ASIN_dict

    def get_Product_Introduction(self):
        '''
        获取产品介绍
        :return:
        '''
        Product_Introduction_xpath_list = [

            '//*[@id="feature-bullets"]/ul/li/span/text()',
            '//*[@id="fbExpandableSectionContent"]/ul/li//text()'
        ]

        product_introduction = 'N.A'
        for xpath in Product_Introduction_xpath_list:
            Product_Introduction_result_list = self.etree_html.xpath(xpath)
            if Product_Introduction_result_list:
                product_introduction = []
            for introduction in Product_Introduction_result_list:
                introduction = introduction.replace('\n','').replace('  ','').replace('\t','')
                if introduction:
                    product_introduction.append(introduction)

        return product_introduction

    def get_Product_description(self):
        '''
        获取产品描述
        :return:
        '''
        Product_description_xpath_list = [
            '//div[@id="productDescription"]/p//text()',
            '//div[@id="productDescription"]/text()'
        ]

        Product_description_re_list = [
            'div id="productDescription" class="a-section a-spacing-small">[\s\S]*?<p>([\s\S]*?)</p>'
        ]

        Product_description = []
        for xpath in Product_description_xpath_list:
            Product_description_result_list = self.etree_html.xpath(xpath)
            print('Product_description_result_list',Product_description_result_list)
            if Product_description_result_list:
                for product_description in Product_description_result_list:
                    product_description = product_description.replace('  ','').replace('\n','').replace('\t','')
                    if product_description:
                        Product_description.append(product_description)
                break
            else:
                pass

        if not Product_description:

            for re_exp in Product_description_re_list:
                Product_description_result_list = re.findall(re_exp,self.response)
                if Product_description_result_list:
                    for product_description in Product_description_result_list:
                        product_description = product_description.replace('  ', '').replace('\n', '').replace('\t', '')
                        if product_description:
                            Product_description = product_description.replace('</br>','').replace('<P>','')\
                                .replace('<b>','').replace('</b>','').split('<br>')
                    break

        return Product_description





def create_USA_analysis_obj(all_response, url):
    '''
    创建一个 USAgetinfo　类对象，usa_product_obj提供使用者调用（use_analysis.py 调用）
    :param all_response:
    :param url:
    :return sa_product_obj:
    '''
    usa_product_obj = USAgetinfo(all_response, url)
    return usa_product_obj



class USAsecondgetinfo():

    def __init__(self,product_info):
        self.product_info = product_info


    def Usually(self):
        '''
        显示库存为　Usually ship whit x to x day 时对库存的取值处理
        :return:
        '''
        self.product_info['Stock'] = -3

    def Only(self,stock):
        '''
        显示库存为　Only x left in stock 时对库存的取值处理
        :param stock:
        :return:
        '''
        try:
            self.product_info['Stock'] = re.findall('\d+', stock)[0]
        except Exception as e:
            self.product_info['Stock'] = -4


    def Stock(self,ASIN,offerListingID):
        '''
        显示库存为 In stock 时对库存取值处理
        :param ASIN:
        :param offerListingID:
        :return:
        '''
        for i in range(3):
            try:
                add_cart_responses = add_Cart(ASIN=ASIN, offerListingID=offerListingID)
            except Exception as e:
                logger.exception('add_cart_response')

            print('into stock')

            add_OK_re_list = [
                                'Added to Cart',
                                'added to Cart'
                            ]

            add_NO_re_list = [
                                'There was a problem adding these items to Cart',
                                'Not added'
                            ]

            get_stock_re_list = [
                                'only\s*(\d*)\s*of',
                                'the\s*(\d.*?)\s*available ',
                            ]

            for re_exp in add_OK_re_list:
                add_OK_status = re.findall(re_exp, add_cart_responses)
                print('into add  OK:',add_OK_status)
                if add_OK_status:
                    self.product_info['Stock'] = -9
                    break

            if not add_OK_status:
                for re_exp in get_stock_re_list:
                    Stock_list = re.findall(re_exp, add_cart_responses)
                    print('Stock_list:', Stock_list)
                    if Stock_list:
                        self.product_info['Stock'] = Stock_list[0]
                        break

                    elif re.findall('limit of', add_cart_responses):
                        ##限制购买数量，无法显示　库存
                        self.product_info['Stock'] = -2
                        break

                    else:
                        ##获取失败，没有匹配到内容
                        self.product_info['Stock'] = -1

            if self.product_info['Stock'] != -1:
                break


    def Available(self,sellers_list_url,ASIN,timeout=20):


        try:
            sellers_list_responses = into_Sellers_list(sellers_list_url)
        except Exception as e:
            logger.exception('sellers_list_responses')

        print('pass into_Sellers_list')
        etree_html = etree.HTML(sellers_list_responses)

        self.product_info['Stock'] = -7
        try:
            for nub in range(2, 11):

                get_Price_xpath_list = [
                    '//*[@id="olpOfferList"]/div/div/div[' + str(nub) + ']/div[1]/span/text()',
                ]

                get_Ship_xpath_list = [
                    '//*[@id="olpOfferList"]/div/div/div[' + str(nub) + ']/div[1]/span[2]/@class',
                ]

                get_New_xpath_list = [
                    '//*[@id="olpOfferList"]/div/div/div[' + str(nub) + ']/div[2]/div/span/text()',
                ]

                get_Seller_xpath_list = [
                    #美国和英国的位置有不同
                    '//*[@id="olpOfferList"]/div/div/div[' + str(nub) + ']/div[4]/h3/span/a/text()',
                    #英国
                    # '//*[@id="olpOfferList"]/div/div/div[' + str(nub) + ']/div[3]/h3/span/a/text()',
                ]

                get_offeringID_xpath_list = [
                    '//*[@id="olpOfferList"]/div/div/div[' + str(nub) + ']/div[5]/div/form/input[9]/@value',
                ]

                for xpath in get_New_xpath_list:
                    New_list = etree_html.xpath(xpath)
                    if New_list:
                        New = New_list[0].replace(' ', '').replace('\n', '')
                    print('New', New)

                if New != 'New':
                    continue

                for xpath in get_Price_xpath_list:
                    Price_list = etree_html.xpath(xpath)
                    print('Price_list:', Price_list)
                    if Price_list:
                        try:
                            Price = float(
                                Price_list[0].replace('$', '').replace(' ', '').replace('\n', '').replace(',', ''))
                            break
                        except Exception as e:
                            print(e)
                            Price = -4
                    else:
                        Price = -1
                self.product_info['Price'] = Price
                print('Price:', Price)

                for xpath in get_Ship_xpath_list:
                    Ship_list = etree_html.xpath(xpath)
                    if Ship_list:
                        Ship = 'FBA'
                    else:
                        Ship = 'FBM'
                self.product_info['Ship'] = Ship
                print('Ship:', Ship)

                for xpath in get_Seller_xpath_list:
                    Seller_list = etree_html.xpath(xpath)
                    if Seller_list:
                        Seller = Seller_list[0].replace('  ', '').replace('\n', '')
                        break
                    else:
                        Seller = ' Amazon.'
                self.product_info['Seller'] = Seller
                print('Seller:', Seller)

                for xpath in get_offeringID_xpath_list:
                    offeringID_list = etree_html.xpath(xpath)
                    if offeringID_list:
                        offeringID = offeringID_list[0]
                        break
                    else:
                        offeringID = '-1'
                self.Stock(ASIN=ASIN, offerListingID=offeringID)
                print('offeringID', offeringID)
                break

        except Exception as e:
            print(e)
            self.product_info['Stock'] = -6



    def Unavaible(self):
        self.product_info['Stock'] = 0
        pass

    def NA(self):
        self.product_info['Stock'] = -5
        pass



def USA_second_Analysis(ASIN, stock, sellers_list_url, product_info,offerListingID):
    '''
    没有环境黄金购物车时，进行二次获取信息
    :param ASIN:
    :param Stock:
    :return:
    '''
    print('into second')

    usa_second_product_obj = USAsecondgetinfo(product_info=product_info)

    if 'Usually' in stock or 'ship' in stock:
        print('into Usually')
        usa_second_product_obj.Stock(ASIN=ASIN, offerListingID=offerListingID)

    elif 'Only' in stock:
        print('into only')
        usa_second_product_obj.Only(stock=stock)

    elif stock == 'In Stock.' or stock == 'In stock.':
        print('into Stock')
        usa_second_product_obj.Stock(ASIN=ASIN,offerListingID=offerListingID)


    elif 'Available' in stock:
        print('into Available')
        usa_second_product_obj.Available(sellers_list_url=sellers_list_url,ASIN=ASIN)


    elif 'unavailable' in stock or 'Unavailable' in stock:
        print('into unavailable')
        usa_second_product_obj.Unavaible()

    else:
        usa_second_product_obj.NA()

    return stock





