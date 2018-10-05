
class REHANDLE():

    def Check_OK(self,product_info,redsi_obj):
        '''
        检验信息获取是否出现异常
        :param product_info:
        :return　Ture or Fales:
        '''
        Brand = product_info['Brand']
        Title = product_info['Title']
        Rating = product_info['Rating']
        Price = product_info['Price']
        Sellers = product_info['Sellers']
        Dimensions = product_info['Dimensions']
        Weigth = product_info['Weigth']
        Reviews = product_info['Reviews']
        Seller = product_info['Seller']
        big_Category = product_info['big_Category']
        big_Ranking = product_info['big_Ranking']
        Stock = product_info['Stock']

        if Brand=='N.A' and Title=='N.A' and Rating==0 and Price==-1.0 and Sellers==-1 and Dimensions=='N.A' and Weigth=='N.A' and \
            Reviews==0 and Seller=='N.A' and big_Category=='N.A' and big_Ranking==-1:
            return False

        elif Stock == -1:
            return False

        else:
            return True


repeat_handle_obj = REHANDLE()