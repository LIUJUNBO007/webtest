'''
文件名:AddProductsAttributePage.py
后台管理-->添加新商品-->商品属性的page类
作者:严晓艺
'''
from Common.Base import Base,open_browser
class AddProductsAttribute(Base):
    '''封装页面表现层,制作页面元素定位器'''
    #1.商品类型选择框定位器
    choose_product_type_loc=('name','goods_type')
    #2.确定按钮定位器
    confirm_button_loc=('css selector','input[value=" 确定 "]')
    #3.重置按钮定位器
    reset_button_loc=('css selector','input[value=" 重置 "]')