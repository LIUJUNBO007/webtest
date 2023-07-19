"""
文件名: BackStageLoginPage.py
作用: 对后台登录页面进行封装
    封装内容: 页面的表现层和操作层
    Page类: 继承Base类
"""
from Common.Base import Base, open_browser

login_url = 'http://localhost:8082/ecshop/admin/privilege.php?act=login'


class BackStageLoginPage(Base):
    """封装页面表现层: 制作页面元素的定位器"""
    ecshop_button_loc = ('id', 'cloudLogin')  # ecshop登录按钮定位器
    username_loc = ('name', 'username')  # 用户名输入框
    password_loc = ('name', 'password')  # 密码输入框
    submit_loc = ('class name', 'btn-a')  # 立即登录按钮
    result_loc = ('css selector', 'main-frame')  # 登录结果
    """封装操作层: 对表现层元素的操作"""

    def click_ecshop(self):
        '''
        点击ecshop进入登录页面
        :return:
        '''
        self.click(self.ecshop_button_loc)

    def input_username(self, username):
        """
        输入用户名
        :param username: 用户名
        :return:
        """
        self.send_keys(text=username, locator=self.username_loc)

    def input_password(self, password):
        """
        输入密码
        :param password: 密码
        :return:
        """
        self.send_keys(text=password, locator=self.password_loc)

    def click_submit(self):
        """
        点击登录按钮
        :return:
        """
        self.click(self.submit_loc)

    def is_login_success(self, username):
        """
        判断是否登录成功
        :return:
        需要一个判断元素文本是否和给定的文本一致
        """
        return self.is_text_in_element(text=username, locator=self.result_loc)


if __name__ == '__main__':
    import time

    login = BackStageLoginPage(open_browser())  # 打开浏览器
    login.open_url(login_url)  # 进入登录页面
    login.remove_alerta_window(id='CMask')
    login.remove_alerta_window(id='panelCloud')
    # 0.点击ecshop登录按钮
    login.click_ecshop()
    time.sleep(2)
    # 1.输入用户名
    username = 'it'
    login.input_username(username)
    # 2.输入密码
    password = 'it123456'
    login.input_password(password)
    # 4.点击立即登录
    login.click_submit()
    time.sleep(5)
    # 5.关闭浏览器
    login.close_browser()
