"""
文件名: LoginPage.py
作用: 对登录页面进行封装
    封装内容: 页面的表现层和操作层
    Page类: 继承Base类
"""
from Common.Base import Base, open_browser

login_url = 'http://localhost:8082/ecshop/user.php'


class LoginPage(Base):
    """封装页面表现层: 制作页面元素的定位器"""
    username_loc = ('name', 'username')  # 用户名输入框
    password_loc = ('name', 'password')  # 密码输入框
    remember_loc = ('id', 'remember')  # 记住密码
    submit_loc = ('class name', 'us_Submit')  # 立即登录按钮
    question_loc = ('link text', '密码问题')  # 找回密码_密码问题
    email_loc = ('link text', '邮件')  # 找回密码_邮件
    register_loc = ('css selector','.usTxt>a')
    """封装操作层: 对表现层元素的操作"""

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

    def remember_password(self):
        """
        点击记住密码
        :return:
        """
        self.click(self.remember_loc)

    def click_submit(self):
        """
        点击登录按钮
        :return:
        """
        self.click(self.submit_loc)

    def click_register(self):
        """
        点击立即注册
        :return:
        """
        self.click(self.register_loc)


if __name__ == '__main__':
    import time
    login = LoginPage(open_browser())  # 打开浏览器
    login.open_url(login_url)  # 进入登录页面
    # # 1.输入用户名
    # username = '诸葛亮'
    # login.input_username(username)
    # # 2.输入密码
    # password = '123456'
    # login.input_password(password)
    # # 3.点击记住密码
    # login.remember_password()
    # # 4.点击立即登录
    # login.click_submit()
    login.click_register()
    time.sleep(5)
    # 5.关闭浏览器
    login.close_browser()
