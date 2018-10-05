

from lxml import etree


def Available_handle(sellers_list_responses):

    etree_html = etree.HTML(sellers_list_responses)

    for nub in range(2,11):

        get_Price_xpath_list = [
            '//*[@id="olpOfferList"]/div/div/div['+ str(nub) +']/div[1]/span/text()',
        ]

        get_Ship_xpath_list = [
            '//*[@id="olpOfferList"]/div/div/div['+ str(nub) +']/div[1]/span[2]/@class',
        ]

        get_New_xpath_list = [
            '//*[@id="olpOfferList"]/div/div/div['+ str(nub) +']/div[2]/div/span/text()'
        ]

        get_Seller_xpath_list = [
            '//*[@id="olpOfferList"]/div/div/div['+ str(nub) +']/div[3]/h3/span/a/text()',
        ]

        get_offeringID_xpath_list = [
            '//*[@id="olpOfferList"]/div/div/div['+ str(nub) +']/div[5]/div/form/input[9]/@value'
        ]

        for xpath in get_New_xpath_list:
            New_list = etree_html.xpath(xpath)
            if New_list:
                New = New_list[0].replace(' ', '').replace('\n', '')
            print('New',New)

        if New != 'New':
            continue

        for xpath in get_Price_xpath_list:
            Price_list = etree_html.xpath(xpath)
            print('Price_list:',Price_list)
            if Price_list:
                try:
                    Price = float(Price_list[0].replace('£', '').replace(' ', '').replace('\n', '').replace(',', ''))
                except Exception as e:
                    print(e)
                    Price = -4
            else:
                Price = -1
            print('Price:',Price)

        for xpath in get_Ship_xpath_list:
            Ship_list = etree_html.xpath(xpath)
            if Ship_list:
                Ship = 'FBA'
            else:
                Ship = 'FBM'
            print('Ship:',Ship)

        for xpath in get_Seller_xpath_list:
            Seller_list = etree_html.xpath(xpath)
            if Seller_list:
                Seller = Seller_list[0].replace('  ', '').replace('\n', '')
            else:
                Seller = ' Amazon.'
            print('Seller:',Seller)

        for xpath in get_offeringID_xpath_list:
            offeringID_list = etree_html.xpath(xpath)
            if offeringID_list:
                offeringID = offeringID_list[0]
            else:
                offeringID = '-1'
            print('offeringID',offeringID)

        break

        # # show_responses_html(responses=sellers_list_responses)
        # seller_allinfo_re_list = [
        #     ##出现匹配失效
        #     '   \$[0-9].\.[0-9]* *[\s\S]*?New[\s\S]*?olpSellerName[\s\S]*?<[\s\S]*?<[\s\S]*?>[\s\S]*?<[\s\S]*?from seller [\s\S]*?and price [\s\S]*?<',
        #     '\d+\.\d\d|\s*?<[\s\S]*?<span class="a-size-medium olpCondition a-text-bold">\n\n\s*?New\n\s*?</span>[\s\S]*?class="a-offscreen"">from seller [\s\S]*?and price [\s\S]*?<'
        # ]
        #
        # get_price_seller_re_list = [
        #     '   \$[0-9].\.[0-9]* *[\s\S]*?New[\s\S]*?olpSellerName[\s\S]*?<[\s\S]*?<[\s\S]*?>[\s\S]*?<[\s\S]*?from seller ([\s\S]*?)and price ([\s\S]*?)<',
        #     '\d+\.\d\d|\s*?<[\s\S]*?<span class="a-size-medium olpCondition a-text-bold">\n\n\s*?New\n\s*?</span>[\s\S]*?class="a-offscreen"">from seller ([\s\S]*?)and price ([\s\S]*?)<'
        # ]
        #
        # get_offeringID_re_list = [
        #     '"offeringID.1" value="([\s\S]*?)"'
        # ]
        #
        # get_Ship_re_list = [
        #     'supersaver'
        # ]
        #
        # Stock_re_list = [
        #     'only\s*\d*\s*of',
        #     'limit of'
        # ]
        #
        # #设置超时时间，匹配超过２０秒则发出信号
        # signal.alarm(timeout)

        # for re_exp in seller_allinfo_re_list:
        #     seller_info_result_list = re.findall(re_exp, sellers_list_responses)
        #     for re_exp in get_offeringID_re_list:
        #         try:
        #             offeringID = re.findall(re_exp, seller_info_result_list[0])[0]
        #         except Exception as e:
        #             offeringID = '-1'
        #         print('offeringID:', offeringID)
        #
        #     ##获取seller,price
        #     if seller_info_result_list:
        #
        #         for re_exp in get_price_seller_re_list:
        #
        #             get_price_seller_result_list = re.findall(re_exp, seller_info_result_list[0])
        #
        #             if get_price_seller_result_list:
        #                 print(get_price_seller_result_list[0])
        #                 try:
        #                     self.product_info['Price'] = get_price_seller_result_list[0][1].replace('  ', '').replace(
        #                         '\n', '').replace(',', '')[1:]
        #                 except IndexError as e:
        #                     self.product_info['Price'] = '-4'
        #
        #                 try:
        #                     Seller = get_price_seller_result_list[0][0].replace('  ', '').replace('\n', '')
        #                     self.product_info['Seller'] = Seller
        #                 except IndexError as e:
        #                     Seller = '-4'
        #
        #                 break
        #
        #         ##判断ship
        #         for re_exp in get_Ship_re_list:
        #             Ship_result_list = re.findall(re_exp, seller_info_result_list[0])
        #             if Ship_result_list:
        #                 self.product_info['Ship'] = 'FBA'
        #             else:
        #                 self.product_info['Ship'] = 'FBM'
        #
        #         ##获取库存
        #         self.Stock(ASIN=ASIN, offerListingID=offeringID)
        #         break