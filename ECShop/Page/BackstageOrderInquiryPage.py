"""
author:刘俊波
"""
import time

from Common.Base import Base, open_browser
from Page.BackStageLoginPage import BackStageLoginPage

login_url = 'http://localhost:8082/ecshop/admin/'
frame_loc = ('id', 'main-frame')


# Base.click_iframe(locator_iframe=frame_loc,locator=frame_loc)
# Base.click(locator=frame_loc)
# Base.enter_iframe(locator=frame_loc)
# Base.click_iframe(locator=frame_loc,locator_iframe=frame_loc)
class OrderInquoryPage(BackStageLoginPage):
    frame_loc = ('id', 'main-frame')
    # 1.订单号
    order_sn_loc = ('id', 'order_sn')
    # 2.电子邮件
    email_loc = ('id', 'email')
    # 3.购货人
    purchaser_loc = ('id', 'user_name')
    # 4.收货人
    consignee_loc = ('id', 'consignee')
    # 5.地址
    address_loc = ('id', 'address')
    # 6.邮编
    zip_code_loc = ('id', 'zipcode')
    # 7.电话
    tel_loc = ('id', 'tel')
    # 8.手机
    mobile_loc = ('id', 'mobile')
    # 9.1收货地区1
    add_1_loc = ('id', 'selCountries')
    # 9.2收获地区2
    add_2_loc = ('id', 'selProvinces')
    # 9.3收货地区3
    add_3_loc = ('id', 'selCities')
    # 9.4收货地区4
    add_4_loc = ('id', 'selDistricts')
    # 10.配送方式
    distribution_mode_loc = ('id', 'select4')
    # 10.1支付方式
    distribution_pay_loc = ('id', 'select5')
    # 11.下单起始时间
    order_start_time_loc = ('id', 'start_time_id')
    # 12.下单结束时间
    order_end_time_loc = ('id', 'end_time_id')
    # 13.订单状态
    order_status_loc = ('id', 'select9')
    # 14.付款状态
    payment_status_loc = ('id', 'select11')
    # 15.发货状态
    shipment_status_loc = ('id', 'select10')
    # 16.搜索按钮
    search_button_loc = ('id', 'query')
    # 17.重置按钮
    reset_button_loc = ('id', 'reset')

    def send_order_sn(self, order_sn):
        self.send_keys(text=order_sn, locator=self.order_sn_loc)

    def send_email(self, email):
        self.send_keys(text=email, locator=self.email_loc)

    def send_purchaser(self, purchaser):
        self.send_keys(text=purchaser, locator=self.purchaser_loc)

    def send_consignee(self, consignee):
        self.send_keys(text=consignee, locator=self.consignee_loc)

    def send_address(self, address):
        self.send_keys(text=address, locator=self.address_loc)

    def send_zip_code(self, zip_code):
        self.send_keys(text=zip_code, locator=self.zip_code_loc)

    def send_tel(self, tel):
        self.send_keys(text=tel, locator=self.tel_loc)

    def send_mobile(self, mobile):
        self.send_keys(text=mobile, locator=self.mobile_loc)

    def select_add_1(self, index):
        self.select_pull_down_element(index=index, locator=self.add_1_loc)

    def select_add_2(self, index):
        self.select_pull_down_element(index=index, locator=self.add_2_loc)

    def select_add_3(self, index):
        self.select_pull_down_element(index=index, locator=self.add_3_loc)

    def select_add_4(self, index):
        self.select_pull_down_element(index=index, locator=self.add_4_loc)

    def send_distribution_mode_loc(self, distribution_mode):
        self.send_keys(text=distribution_mode, locator=self.distribution_mode_loc)

    def send_distribution_pay(self, distribution_pay):
        self.send_keys(text=distribution_pay, locator=self.distribution_pay_loc)

    def send_order_start_time(self, order_start_time):
        self.send_keys_data(text=order_start_time, locator=self.order_start_time_loc, id='start_time_id')

    def send_order_end_time(self, order_end_time):
        self.send_keys_data(text=order_end_time, locator=self.order_end_time_loc, id='end_time_id')

    def select_order_status(self, index):
        self.select_pull_down_element(index=index, locator=self.order_status_loc)

    def select_payment_status(self, index):
        self.select_pull_down_element(index=index, locator=self.payment_status_loc)

    def select_shipment_status(self, index):
        self.select_pull_down_element(index=index, locator=self.shipment_status_loc)

    def click_search_button(self):
        self.click(locator=self.search_button_loc)

    def click_reset_button(self):
        self.click(locator=self.reset_button_loc)


if __name__ == '__main__':
    login = OrderInquoryPage(open_browser())  # 打开浏览器
    login.open_url(login_url)  # 进入登录页面
    login.remove_alerta_window(id='CMask')
    login.remove_alerta_window(id='panelCloud')
    # 0.点击ecshop登录按钮
    login.click_ecshop()
    time.sleep(2)
    # 1.输入用户名
    username = 'admin'
    login.input_username(username)
    # 2.输入密码
    password = 'pai3.141592653'
    login.input_password(password)
    # 4.点击立即登录
    login.click_submit()
    # login.enter_iframe(('id','menu-frame'))
    login.click_iframe(locator_iframe=('id', 'menu-frame'), locator=('css selector', '[key="04_order"]'))
    login.click_iframe(locator_iframe=('id', 'menu-frame'), locator=('link text', '订单查询'))
    login.send_keys_iframe(locator_iframe=('id', 'main-frame'), locator=('id', 'order_sn'), text=1231332)
    login.enter_iframe(('id', 'main-frame'))
    # login.send_email(email=12345)
    login.send_order_start_time(order_start_time=231131)
    # login.send_email()
    # 5.关闭浏览器
    time.sleep(5)
    login.close_browser()
