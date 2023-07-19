'''
文件名:AddProductsAlbumPage.py
后台管理-->添加新商品-->商品相册的page类
作者:严晓艺
'''
from Common.Base import Base, open_browser


class AddProductsAlbum(Base):
    '''
     封装页面表现层,制作页面元素定位器
    '''
    # 1.图片描述定位器
    photo_description_loc = ('name', 'img_desc[]')
    # 2.选择文件定位器
    choose_file_loc = ('name', 'img_url[]')
    # 3.确定按钮定位器
    confirm_button_loc = ('css selector', 'input[value=" 确定 "]')
    # 4.重置按钮定位器
    reset_button_loc = ('css selector', 'input[value=" 重置 "]')
