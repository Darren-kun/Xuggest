

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 29 14:39:51 2018

@author: Darren_KUN
"""
from AMA_ANALYSIS.DE_analysis import create_DE_analysis_obj,DE_second_Analysis
from AMA_ANALYSIS.UK_analysis import create_UK_analysis_obj, UK_second_Analysis
from AMA_ANALYSIS.USA_analysis import create_USA_analysis_obj,USA_second_Analysis
from ama_blog import logger


class USEANALYSIS():

    '''
    该类封装了　各国家amazon网站解析模块　各数据的解析逻辑调用，和数据整 合返回
    '''

    def USA_analysis(self,all_response, url):
        '''
        获取商品全部信息(图片获取单独调用)
        in:all_response,url
        out:product_info
        '''
        try:
            product_info = {}
            usa_product_obj = create_USA_analysis_obj(all_response,url)

            #    Picture，Brand，Title，Rating，Reviews，Price，Stock，Seller，Sellers，Dimensions，Weigth，ASIN, Ranking, Category
            product_info['Brand'] = usa_product_obj.get_Brand()
            product_info['Title'] = usa_product_obj.get_Title()

            product_info['Reviews'] = usa_product_obj.get_Reviews()
            if product_info['Reviews'] == 0:
                product_info['Rating'] = 0
                product_info['Answered'] = 0
            else:
                product_info['Rating'] = usa_product_obj.get_Rating()

                product_info['Answered'] = usa_product_obj.get_Answered()

            product_info['Price'] = usa_product_obj.get_Price()
            product_info['Seller'] = usa_product_obj.get_Seller()
            product_info['Sellers'] = usa_product_obj.get_Sellers()
            product_info['Dimensions'] = usa_product_obj.get_Dimensions()
            product_info['Size'] = usa_product_obj.get_Size()
            product_info['Weigth'] = usa_product_obj.get_Weigth()
            product_info['ASIN'], product_info['Country'] = usa_product_obj.get_ASIN_country()
            # product_info['Ranking'] = usa_product_obj.get_Ranking()
            # product_info['Category'] = usa_product_obj.get_Category()

            product_info['s_Ranking_Category'] = usa_product_obj.get_s_Ranking_Category()
            product_info['big_Ranking'],product_info['big_Category'] = usa_product_obj.get_big_Ranking_Category()
            product_info['Stock'] = usa_product_obj.get_Stock()
            product_info['Ship'] = usa_product_obj.get_Ship()
            product_info['Color'] = usa_product_obj.get_Product_Color()
            product_info['Product_Introduction'] = usa_product_obj.get_Product_Introduction()
            product_info['Product_description'] = usa_product_obj.get_Product_description()
            product_info['url'] = url
            product_info['Link_ASIN'] = usa_product_obj.get_Link_ASIN()
            #推荐商品的图片url和对应商品url
            product_info['Recommend_product_url_list'] = usa_product_obj.get_Recommend_product_url()
            #
            # Recommend_product_url_list = product_info['Recommend_product_url_list']
            # product_info['recommend_url_nub'] = len(Recommend_product_url_list)

            product_info['Picture_url'] = usa_product_obj.get_Picture_url()
            ##获取Stock的准确值
            offerListingID = usa_product_obj.get_offerListingID()
            print('offerListingID:',offerListingID)
            Stock = product_info['Stock']
            ASIN = product_info['ASIN']
            print(Stock)
            sellers_list_url = usa_product_obj.get_Sellers_url()
            print('sellers_list_url',sellers_list_url)
            try:
                USA_second_Analysis(ASIN=ASIN,stock=Stock,sellers_list_url=sellers_list_url,product_info=product_info,offerListingID=offerListingID)
            except Exception as e:
                logger.exception('USA_USA_second_Analysis')

            if product_info['Size'] == 'Select':
                product_info['Stock'] == -6
            return product_info
        except Exception as e:
            logger.exception('use_USA')


    def UK_analysis(self, all_response, url):
        '''
        获取商品全部信息(图片获取单独调用)
        in:all_response,url
        out:product_info
        '''
        product_info = {}
        uk_product_obj = create_UK_analysis_obj(all_response, url)

        #    Picture，Brand，Title，Rating，Reviews，Price，Stock，Seller，Sellers，Dimensions，Weigth，ASIN, Ranking, Category
        product_info['Brand'] = uk_product_obj.get_Brand()
        product_info['Title'] = uk_product_obj.get_Title()

        product_info['Reviews'] = uk_product_obj.get_Reviews()
        if product_info['Reviews'] == 0:
            product_info['Rating'] = 0
            product_info['Answered'] = 0
        else:
            product_info['Rating'] = uk_product_obj.get_Rating()
            product_info['Answered'] = uk_product_obj.get_Answered()

        product_info['Price'] = uk_product_obj.get_Price()
        product_info['Seller'] = uk_product_obj.get_Seller()
        product_info['Sellers'] = uk_product_obj.get_Sellers()
        product_info['Dimensions'] = uk_product_obj.get_Dimensions()
        product_info['Size'] = uk_product_obj.get_Size()
        product_info['Weigth'] = uk_product_obj.get_Weigth()
        product_info['ASIN'], product_info['Country'] = uk_product_obj.get_ASIN_country()
        # product_info['Ranking'] = usa_product_obj.get_Ranking()
        # product_info['Category'] = usa_product_obj.get_Category()

        product_info['s_Ranking_Category'] = uk_product_obj.get_s_Ranking_Category()
        product_info['big_Ranking'],product_info['big_Category'] = uk_product_obj.get_big_Ranking_Category()
        product_info['Stock'] = uk_product_obj.get_Stock()
        product_info['Ship'] = uk_product_obj.get_Ship()
        product_info['Color'] = uk_product_obj.get_Product_Color()
        product_info['Product_Introduction'] = uk_product_obj.get_Product_Introduction()
        product_info['Product_description'] = uk_product_obj.get_Product_description()
        product_info['url'] = url
        product_info['Link_ASIN'] = uk_product_obj.get_Link_ASIN()
        #推荐商品的图片url和对应商品url
        product_info['Recommend_product_url_list'] = uk_product_obj.get_Recommend_product_url()
        #
        # Recommend_product_url_list = product_info['Recommend_product_url_list']
        # product_info['recommend_url_nub'] = len(Recommend_product_url_list)

        Picture_url = uk_product_obj.get_Picture_url()
        product_info['Picture_url'] = str(len(Picture_url))
        ##获取Stock的准确值
        offerListingID = uk_product_obj.get_offerListingID()
        print('offerListingID:',offerListingID)
        Stock = product_info['Stock']
        ASIN = product_info['ASIN']
        print(Stock)
        sellers_list_url = uk_product_obj.get_Sellers_url()
        print('sellers_list_url',sellers_list_url)
        UK_second_Analysis(ASIN=ASIN,stock=Stock,sellers_list_url=sellers_list_url,product_info=product_info,offerListingID=offerListingID)
        return product_info
        return product_info



    # def DE_analysis(self,all_response, url):
    #     '''
    #     获取商品全部信息(图片获取单独调用)
    #     in:all_response,url
    #     out:product_info
    #     '''
    #     product_info = {}
    #     de_product_obj = create_DE_analysis_obj(all_response,url)
    #
    #     product_info['Brand'] = de_product_obj.get_Brand()
    #     product_info['Title'] = de_product_obj.get_Title()
    #
    #     product_info['Reviews'] = de_product_obj.get_Reviews()
    #     if product_info['Reviews'] == 0:
    #         product_info['Rating'] = 0
    #     else:
    #         product_info['Rating'] = de_product_obj.get_Rating()
    #
    #     product_info['Price'] = de_product_obj.get_Price()
    #     product_info['Seller'] = de_product_obj.get_Seller()
    #     product_info['Sellers'] = de_product_obj.get_Sellers()
    #     product_info['Dimensions'] = de_product_obj.get_Dimensions()
    #     product_info['Weigth'] = de_product_obj.get_Weigth()
    #     product_info['ASIN'], product_info['Country'] = de_product_obj.get_ASIN_country()
    #     product_info['Ranking'] = de_product_obj.get_Ranking()
    #     product_info['Category'] = de_product_obj.get_Category()
    #     product_info['Stock'] = de_product_obj.get_Stock()
    #     product_info['Ship'] = de_product_obj.get_Ship()
    #
    #     product_info['Color'] = de_product_obj.get_Product_Color()
    #
    #     product_info['url'] = url
    #     product_info['Link_ASIN'] = de_product_obj.get_Link_ASIN()
    #     #推荐商品的图片url和对应商品url
    #     Recommend_product_url_list = de_product_obj.get_Recommend_product_url()
    #
    #     product_info['recommend_url_nub'] = len(Recommend_product_url_list)
    #     Picture_url = de_product_obj.get_Picture_url()
    #     product_info['Picture_url'] = Picture_url
    #     ##获取Stock的准确值
    #     offerListingID = de_product_obj.get_offerListingID()
    #     print('offerListingID:',offerListingID)
    #     Stock = product_info['Stock']
    #     ASIN = product_info['ASIN']
    #     print(Stock)
    #     sellers_list_url = de_product_obj.get_Sellers_url()
    #     print('sellers_list_url',sellers_list_url)
    #
    #     DE_second_Analysis(ASIN=ASIN,stock=Stock,sellers_list_url=sellers_list_url,product_info=product_info,offerListingID=offerListingID)
    #
    #     return product_info

using_analysis_obj = USEANALYSIS()