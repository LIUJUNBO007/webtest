'''
文件名:AddProductsDetailedDescriptionPage.py
后台管理-->添加新商品-->详细描述的page类
作者:严晓艺
'''
from Common.Base import Base,open_browser
class AddProductsDetailedDescription(Base):
    '''封装页面表现层,制作页面元素定位器'''
    #1.frame1定位器
    frame1_loc=('id','main-frame')
    #2.frame2定位器
    iframe2_loc=('id','goods_desc___Frame')
    #3.输入框定位器
    input_description_loc=('css selector','body[spellcheck="false"]')
    #4.确定按钮定位器
    confirm_button_loc=('css selector','input[value=" 确定 "]')
    #5.重置按钮定位器
    reset_button_loc=('css selector','input[value=" 重置 "]')