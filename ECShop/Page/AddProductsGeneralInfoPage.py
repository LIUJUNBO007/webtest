'''
文件名:AddProductsGeneralInfoPage.py
后台管理-->添加新商品-->通用信息的page类
作者:严晓艺
'''
from Common.Base import Base, open_browser
class AddProductsGeneralInfoPage(Base):
    '''封装页面表现层,制作页面元素的定位器'''
    # 1页面iframe定位器
    frame_loc=('id','main-frame')
    # 2商品名称输入框定位器
    product_name_loc=('name','goods_name')
    # 3字体选择定位器
    fontse_lection=('name','goods_name')
    # 4商品货号定位器
    product_num_loc=('name','goods_sn')
    # 5商品分类定位器
    product_classify_loc=('name','cat_id')
    # 6添加分类选择定位器
    add_classify_loc=('css selector','button[onclick="rapidCatAdd()"]')
    # 7添加分类输入框定位器
    input_classify_loc=('name','addedCategoryName')
    # 8添加分类确定按钮定位器
    add_classify_confirm_loc=('css selector','button[title=" 确定 "]')
    # 9分类管理按钮定位器
    classification_management_loc=('css selector','button[onclick="return goCatPage()"]')
    # 10扩展分类添加按钮定位器
    extended_classify_button_loc=('css selector','input[value="添加"]')
    # 11扩展分类选择框定位器
    choose_extended_classify_loc=('name','other_cat[]')
    # 12商品品牌选择定位器
    choose_product_brand_loc=('name','brand_id')
    # 13添加品牌输入框定位器
    add_brand_loc=('name','addedBrandName')
    # 14添加品牌确定按钮定位器
    confirm_add_brand_loc=('css selector','button[onclick="addBrand()"]')
    # 15品牌管理按钮定位器
    brand_management_loc=('css selector','button[onclick="return goBrandPage()"]')
    # 16选择供货商定位器
    choose_supplier_loc=('css selector','select[name="suppliers_id"]')
    # 17本店售价定位器
    my_shop_loc=('name','shop_price')
    # 18商品优惠价格_优惠数量输入框定位器
    preferential_quantity_loc=('name','volume_number[]')
    # 19商品优惠价格_优惠价格输入框定位器
    favorable_price_loc=('name','volume_price[]')
    # 20市场售价输入框定位器
    market_price_loc=('name','market_price')
    # 21虚拟销量输入框定位器
    virtual_sales_loc=('name','virtual_sales')
    # 22促销价选择框定位器
    promotion_price_loc=('css selector','input[onclick="handlePromote(this.checked);"]')
    # 23促销价输入框定位器
    input_promotion_price_loc=('css selector','input[name="promote_price"]')
    # 24促销起始日期输入框定位器
    promotion_star_date_loc=('id','promote_start_date')
    # 25促销结束日期输入框定位器
    promotion_end_date_loc=('id','promote_end_date')
    # 26上传商品图片,选择文件按钮定位器
    choose_photo_file_loc=('name','goods_img')
    # 27勾选自动生成商品缩略图定位器
    generate_item_thumbnail_loc=('id','auto_thumb')
    # 28确定按钮定位器
    confirm_loc=('css selector','input[value=" 确定 "]')
    # 29重置按钮定位器
    reset_loc=('css selector','input[value=" 重置 "]')
    '''封装操作层,操作元素'''
    def input_product_name(self,product_name):
        '''
        输入商品名称
        :param product_name: 商品名称
        :return: 
        '''
        self.send_keys(text=product_name,button=self.product_name_loc)
