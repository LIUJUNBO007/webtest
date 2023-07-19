'''
文件名:AddProductsOtherInfoPage.py
后台管理-->添加新商品-->其他信息的page类
作者:严晓艺
'''
from Common.Base import Base,open_browser
class AddProductsOtherInfo(Base):
    '''封装页面表现层,制作页面元素定位器'''
    #1.商品重量定位器
    product_weight_loc=('name','goods_weight')
    #2.重量选择框定位器
    choose_weight_loc=('name','weight_unit')
    #3.商品库存数量定位器
    stocks_loc=('name','goods_number')
    #4.库存警告数量定位器
    stocks_warning_loc=('name','warn_number')
    #5.加入推荐:精品选择框定位器
    choose_boutique_loc=('name','is_best')
    #6.加入推荐:新品选择框定位器
    choose_new_product_loc=('name','is_new')
    #7.加入推荐:热销选择框定位器
    choose_hot_sale_loc=('name','is_hot')
    #8.是否上架选择框定位器
    choose_on_the_shelf_loc=('name','is_on_sale')
    #7.作为普通商品销售选择框定位器
    choose_general_product_loc=('name','is_alone_sale')
    #8.免运费商品选择框
    no_freight_loc=('name','is_shipping')
    #9.商品关键词输入框定位器
    product_keyword_loc=('name','keywords')
    #10.商品简单描述输入框定位器
    product_simple_description_loc=('name','goods_brief')
    #11.商家备注输入框定位器
    business_comments_loc=('name','seller_note')
    #12.确定按钮定位器
    confirm_button_loc = ('css selector', 'input[value=" 确定 "]')
    #13.重置按钮定位器
    reset_button_loc = ('css selector', 'input[value=" 重置 "]')