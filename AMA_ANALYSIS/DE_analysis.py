# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 22:13:07 2018

@author: PC1
"""

# -*- coding: utf-8 -*-


"""
Created on Wed Aug 29 14:39:51 2018

@author: Darren_KUN
"""

import re
from lxml import etree
# from AMAZONscrapy.AMAZONscrapy.AMA_ANALYSIS.analysis_request_header import add_Cart,into_Sellers_list, updata_Shopping_nub
# from AMAZONscrapy.AMAZONscrapy.AMA_ANALYSIS_TEST.show_respones_html import show_responses_html
from AMA_ANALYSIS.analysis_request_header import add_Cart,into_Sellers_list, updata_Shopping_nub
from AMA_ANALYSIS_TEST.show_respones_html import show_responses_html


class DEgetinfo():
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
        # show_responses_html(self.response)
        Sellers_url_xpath_list = [
            '//*[@id="olp_feature_div"]/div/span[1]/a/@href',

        ]

        Sellers_url_re_list = [
            '''class="a-size-small aok-float-right a-center"><a href="([\s\S]*?)"''',
            'a href="[\s\S]*?"><b>New</b> \((\d.*)\) ',
            '\(3\) '
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
            if len(offerlistID_result_list) == 1:
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

        for xpath in Brand_xpath_list:
            Brand_result_list = self.etree_html.xpath(xpath)
            if len(Brand_result_list) == 1:
                Brand = Brand_result_list[0]
                break
            else:
                Brand = 'N.A'

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

        for xpath in Title_xpath_list:
            Title_result_list = self.etree_html.xpath(xpath)
            if len(Title_result_list) == 1:
                Title = Title_result_list[0].replace('\n', '').replace('  ', '')
                break
            Title = 'N.A'

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
                print(re.findall(re_exp,Rating))
                try:
                    Rating = float(re.findall(re_exp,Rating)[0])
                except IndexError as e:
                    continue

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
            '([\s\S]*?) customer reviews'
        ]
        Reviews = 'N.A'
        for xpath in Reviews_xpath_list:
            Reviews_result_list = self.etree_html.xpath(xpath)
            if len(Reviews_result_list) == 1:
                Reviews = Reviews_result_list[0]
                break
        if Reviews == 'N.A':
            for re_exp in Reviews_re_list:
                Reviews_result_list = re.findall(re_exp, self.response)
                if len(Reviews_result_list) > 0:
                    Reviews = Reviews_result_list[0]

                else:
                    Reviews = 0

        if Reviews != 'N.A':
            for re_exp in get_end_number_re_list:
                try:
                    Reviews = re.findall(re_exp, Reviews)[0]
                except Exception as e:
                    pass
        return Reviews


    def get_Price(self):
        '''
        获取价格
        '''
        Price_xpath_list = [
            '//*[@id="priceblock_dealprice"]/text()',
            '//*[@id="priceblock_ourprice"]/text()',
            '//*[@id="price_inside_buybox"]/text()'
        ]
        Price_re_list = [
            '''id="price_inside_buybox" class="a-size-medium a-color-price">([\s\S]*?)<'''
        ]

        Price = -1
        for xpath in Price_xpath_list:
            Price_result_list = self.etree_html.xpath(xpath)
            if len(Price_result_list) == 1:
                Price = Price_result_list[0][1:]
                break

        if Price == -1:
            for re_exp in Price_re_list:
                Price_result_list = re.findall(re_exp, self.response)

                if len(Price_result_list) == 1:
                    Price = Price_result_list[0].replace(' ', '').replace('\n', '')
                    break

        return Price

    def get_Stock(self):
        '''
        获取库存
        '''
        Stock_xpath_list = [
            '//*[@id="availability"]/span/text()',
        ]
        Stock_re_list = [
            'class="a-size-medium a-color-success">([\s\S]*?)<',
        ]

        Stock = 'N.A'
        for xpath in Stock_xpath_list:
            Stock_result_list = self.etree_html.xpath(xpath)
            if len(Stock_result_list) == 1:
                Stock = Stock_result_list[0].replace('\n', '').replace('  ', '')
                break


        if Stock == 'N.A':
            for re_exp in Stock_re_list:
                Stock_result_list = re.findall(re_exp, self.response)
                if len(Stock_result_list) >= 1:
                    Stock = Stock_result_list[0].replace('\n', '').replace('  ', '')
                    break

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
            '''Ships from and sold by <a href='[\s\S]*?'>([\s\S]*?)</a>''',
            '''Ships from and sold by([\s\S]*?)\.'''
        ]

        for xpath in Seller_xpath_list:
            Seller_result_list = self.etree_html.xpath(xpath)
            if len(Seller_result_list) == 1:
                Seller = Seller_result_list[0].replace('\n', '').replace('  ', '')
                if len(Seller) < 100:
                    break
            Seller = 'N.A'

        if Seller == 'N.A' or 'Fulfilled by Amazon':
            for re_exp in Seller_re_list:
                Seler_result_list = re.findall(re_exp, self.response)
                if len(Seler_result_list) >= 1:
                    Seller = Seler_result_list[0].replace('\n', '').replace('  ', '')
                    if len(Seller) > 30:
                        Seller = 'N.A'
                    else:
                        break

        return Seller

    def get_Sellers(self):
        '''
        获取卖家数量
        '''
        Sellers_xpath_list = [
            '//*[@id="olp_feature_div"]/div/span[1]/a/text()'
        ]

        get_end_number_re_list = [
            '\((\d+)\)'
        ]

        Sellers = -1
        for xpath in Sellers_xpath_list:
            Sellers_result_list = self.etree_html.xpath(xpath)
            if len(Sellers_result_list) == 1:
                Sellers = Sellers_result_list[0]
                break

        if Sellers != -1:
            for re_exp in get_end_number_re_list:
                try:
                    Sellers = int(re.findall(re_exp,Sellers)[0])
                except Exception as e:
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
            '''<td class="a-size-base">([\s\S]*?)</td>''',
            '<td class="a-size-base">\s*?(\d.*?\.\d x[\s\S]*?)<',
            'Size:(\d[\s\S]*?)<',
            '''Product Dimensions: 
    </b>
    ([\s\S]*?)
    </li>'''

        ]

        for re_exp in Dimensions_re_list:
            Dimensions_result_list = re.findall(re_exp, self.response)

            if len(Dimensions_result_list) == 1:

                Dimensions = Dimensions_result_list[0].replace(' ', '').replace('\n', '')
                if len(Dimensions) < 30:
                    break
            elif len(Dimensions_result_list) > 1:

                for Dimensions_result in Dimensions_result_list:

                    if 'x' in Dimensions_result :
                        Dimensions = Dimensions_result.replace(' ', '').replace('\n', '')
                        if len(Dimensions):
                            break
                break
            else:
                Dimensions = 'N.A'

        if Dimensions == 'N.A':
            for xpath in Dimensions_xpath_list:
                Dimensions_result_list = self.etree_html.xpath(xpath)
                if len(Dimensions_result_list) == 1:
                    Dimensions = Dimensions_result_list[0].replace('\n', '').replace('  ', '')
                    break
        return Dimensions

    def get_ASIN_country(self):
        '''
        获取ASIN
        '''
        ASIN_xpath_list = [
            '//*[@id="detail-bullets"]/table/tbody/tr/td/div[2]/ul/li[5]/text()',
            '//*[@id="mbc"]/div/div/h5[1]/span/a/text()'
        ]
        ASIN_re_list = [
            '/([A-Z0-9]+)/',
            '/(B[\s\S]*?)$'
        ]
        country_re_list = [
            'amazon.([\s\S]*?)/'
        ]
        for re_exp in ASIN_re_list:
            ASIN_result_list = re.findall(re_exp, self.product_url)
            if len(ASIN_result_list) == 1:
                ASIN = ASIN_result_list[0]
                break
            ASIN = 'N.A'

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
            'Shipping Weight:</b> ([\s\S]*?[a-z])',
            '<td class="a-size-base">([\s\S]*?)</td>',
            'Shipping Weight[\s\S]*?(\d[\s\S]*?)\('
        ]

        for re_exp in Weigth_re_list:
            Weigth_result_list = re.findall(re_exp, self.response)
            if len(Weigth_result_list) == 1:
                Weigth = Weigth_result_list[0]
                break
            elif len(Weigth_result_list) > 1:

                for Weigth_result in Weigth_result_list:
                    Weigth_list = re.findall('^\d', Weigth_result.replace('\n', '').replace(' ', ''))
                    if len(Weigth_list) > 0 and 'x' not in Weigth_result:
                        Weigth = Weigth_result.replace('\n', '').replace(' ', '')
                        break
                break
            else:
                Weigth = 'N.A'

        if Weigth == 'N.A':
            for xpath in Weigth_xpath_list:
                Weigth_result_list = self.etree_html.xpath(xpath)
                if len(Weigth_result_list) == 1:
                    Weigth = Weigth_result_list[0]
                    break
        return Weigth

    def get_Ranking(self):
        '''
        获取排名
        '''
        Ranking_xpath_list = [
            '//*[@id="SalesRank"]/ul/li[1]/span[1]/text()'
        ]
        Ranking_re_list = [
            '(#\d*|#\d*,\d*) in <'
        ]
        Ranking = 'N.A'
        for xpath in Ranking_xpath_list:
            Ranking_result_list = self.etree_html.xpath(xpath)
            if len(Ranking_result_list) == 1:
                try:
                    Ranking = int(Ranking_result_list[0][1:])
                    break
                except Exception as e:
                    pass


        if Ranking == 'N.A':
            for re_exp in Ranking_re_list:
                Ranking_result_list = re.findall(re_exp, self.response)
                if len(Ranking_result_list) > 0:
                    Ranking = int(Ranking_result_list[0][1:])
                else:
                    Ranking = -1

        return Ranking

    def get_Category(self):
        '''
        获取分类
        '''
        Category_xpath_list = [
            '//*[@id="SalesRank"]/ul/li[1]/span[2]/a[1]/text()'
        ]
        Category_re_list = [
            'href="[\s\S]*?">([A-Z][a-z]*? &[\s\S]*?)<'
        ]

        for xpath in Category_xpath_list:
            Category_result_list = self.etree_html.xpath(xpath)

            if len(Category_result_list) == 1:
                Category = Category_result_list[0]
                break
            Category = 'N.A'

        if Category == 'N.A':
            for re_exp in Category_re_list:
                Category_result_list = re.findall(re_exp, self.response)
                if len(Category_result_list) > 0:
                    Category = Category_result_list[0]

        return Category

    def get_Recommend_product_url(self):
        '''
        获取产品的推荐产品　图片ｕｒｌ和产品ｕｒｌ
        返回的内容　是列表　[(product_url,product_picture_url),(),..]
        :return:Recommend_product_list
        '''
        Recommend_product_list = []
        Recommend_product_re_list = [
            '<a class="a-link-normal" target="_top" rel="noopener" title="[\s\S]*?" href="([\s\S]*?)"[\s\S]*?src="([\s\S]*?)"',
            # '<a class="a-link-normal" href="([\s\S]*?)"[\s\S]*?src="([\s\S]*?)"'
        ]
        for re_exp in Recommend_product_re_list:
            Recommend_product_result_list = re.findall(re_exp, self.response)
            for Recommend_product_result in Recommend_product_result_list:
                Recommend_product_list.append(Recommend_product_result)
        print(len(Recommend_product_list))
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
            if FBA_result:
                break
        for re_exp in FBM_re_list:
            FBM_result = re.findall(re_exp, self.response)
            print('FBM_result',FBM_result)
            if FBM_result:
                break

        if FBA_result:
            if not FBM_result:
                Ship = 'FBA'

        elif FBM_result:
            if not FBA_result:
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
            '//*[@id="variation_color_name"]/div/span/text()'
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
            '//*[@id="color_name_0"]/@data-defaultasin',
            '//*[@id="variation_color_name"]/ul//@data-defaultasin'
        ]

        Link_Size_ASIN_xpath = [
            '//*[@id="native_dropdown_selected_size_name"]//@value'
        ]
        Link_ASIN_dict = {}
        for xpath in Link_Color_ASIN_xpath:
            Link_Color_ASIN_result_list = self.etree_html.xpath(xpath)
            if Link_Color_ASIN_result_list:
                Link_ASIN_dict['Link_Color_ASIN_list'] = Link_Color_ASIN_result_list[1:]
            else:
                Link_ASIN_dict['Link_Color_ASIN_list'] = []

        for xpath in Link_Size_ASIN_xpath:
            Link_Size_ASIN_result_list = self.etree_html.xpath(xpath)
            Link_Size_ASIN_list =[]
            if Link_Size_ASIN_result_list:
                for Link_Size_ASIN in Link_Size_ASIN_result_list[1:]:
                    Link_Size_ASIN_list.append(Link_Size_ASIN[2:])
                Link_ASIN_dict['Link_Size_ASIN_list'] = Link_Size_ASIN_list

            else:
                Link_ASIN_dict['Link_Size_ASIN_list'] = []


        return str(Link_ASIN_dict)


def create_DE_analysis_obj(all_response, url):
    '''
    创建一个 USAgetinfo　类对象，usa_product_obj提供使用者调用（use_analysis.py 调用）
    :param all_response:
    :param url:
    :return sa_product_obj:
    '''
    de_product_obj = DEgetinfo(all_response, url)
    return de_product_obj


def DE_second_Analysis(ASIN, stock, sellers_list_url, product_info,offerListingID):
    '''
    没有环境黄金购物车时，进行二次获取信息
    :param ASIN:
    :param Stock:
    :return:
    '''
    print('into second')

    # show_responses_html(add_cart_responses)

    if 'Usually' in stock or 'ship' in stock:
        print('into usually')
        product_info['Stock'] = 0

    elif 'Only' in stock:
        print('into only')
        product_info['Stock'] = re.findall('\d+', stock)[0]

    elif stock == 'In Stock.' or stock == 'In stock.':
        add_cart_responses = add_Cart(ASIN=ASIN, offerListingID=offerListingID)
        print('into stock')
        add_OK_re_list = [
            'Added to Cart'
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
            print('into add  OK')
            print(add_OK_status)
            if add_OK_status:
                product_info['Stock'] = 99999999
                break

        if not add_OK_status:
            for re_exp in get_stock_re_list:
                Stock_list = re.findall(re_exp, add_cart_responses)
                print('Stock_list:',Stock_list)
                if Stock_list:
                    product_info['Stock'] = Stock_list[0]
                    break

                elif len(re.findall('limit of', add_cart_responses)) > 0:
                    ##限制购买数量，无法显示　库存
                    product_info['Stock'] = '-2'
                    break

                # elif Stock_list:
                #     product_info['Stock'] = Stock_list[0]
                #
                #     break

                else:
                    ##获取失败，没有匹配到内容

                    product_info['Stock'] = '-1'


    elif 'Available' in stock:
        print('into Available')
        sellers_list_responses = into_Sellers_list(sellers_list_url)
        # show_responses_html(responses=sellers_list_responses)
        seller_allinfo_re_list = [
            # '   \$[0-9].\.[0-9]* *[\s\S]*?New[\s\S]*?olpSellerName[\s\S]*?<[\s\S]*?<[\s\S]*?>[\s\S]*?<',
            '\d+\.\d\d|\s*?<[\s\S]*?<span class="a-size-medium olpCondition a-text-bold">\n\n\s*?New\n\s*?</span>[\s\S]*?class="a-offscreen"">from seller [\s\S]*?and price [\s\S]*?<'
        ]

        get_price_seller_re_list = [
            # '   (\$[0-9].\.[0-9]*) *[\s\S]*?New[\s\S]*?olpSellerName[\s\S]*?<[\s\S]*?<[\s\S]*?>([\s\S]*?)<',
            '\d+\.\d\d|\s*?<[\s\S]*?<span class="a-size-medium olpCondition a-text-bold">\n\n\s*?New\n\s*?</span>[\s\S]*?class="a-offscreen"">from seller ([\s\S]*?)and price ([\s\S]*?)<'
        ]

        get_offeringID_re_list = [
            '"offeringID.1" value="([\s\S]*?)"'
        ]

        get_Ship_re_list = [
            'supersaver'
        ]

        Stock_re_list = [
            'only\s*\d*\s*of',
            'limit of'
        ]

        for re_exp in seller_allinfo_re_list:
            seller_info_result_list = re.findall(re_exp, sellers_list_responses)
            for re_exp in get_offeringID_re_list:

                offeringID = re.findall(re_exp, seller_info_result_list[0])[0]
                print('offeringID:',offeringID)
            if seller_info_result_list:

                for re_exp in get_price_seller_re_list:

                    get_price_seller_result_list = re.findall(re_exp, seller_info_result_list[0])

                    if get_price_seller_result_list:
                        print(get_price_seller_result_list[0])
                        product_info['Price'] = get_price_seller_result_list[0][1].replace('  ', '').replace('\n', '')

                        Seller = get_price_seller_result_list[0][0].replace('  ', '').replace('\n', '')

                        if Seller:
                            product_info['Seller'] = Seller

                        else:
                            product_info['Seller'] = ' Amazon.com.'
                        break

                for re_exp in get_Ship_re_list:
                    Ship_result_list = re.findall(re_exp, seller_info_result_list[0])
                    if Ship_result_list:
                        product_info['Ship'] = 'FBA'
                    else:
                        product_info['Ship'] = 'FBM'

        after_updata_responses = updata_Shopping_nub(ASIN,offeringID)
        for re_exp in Stock_re_list:
            Stock_status_list = re.findall(re_exp, after_updata_responses)
            if Stock_status_list:
                if 'only' in Stock_status_list[0]:
                    product_info['Stock'] = re.findall('only\s*(\d*)\s*of', Stock_status_list[0])
                elif 'limit of' in Stock_status_list[0]:
                    product_info['Stock'] = -2
            else:
                product_info['Stock'] = -1


    print('second_Analysis exit')
    return stock




