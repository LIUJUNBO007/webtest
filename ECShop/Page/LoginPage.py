"""
作用:对登录页面进行封装
封装内容:页面的表现曾和操作层
Page类:继承Base类


"""
from Common.Base import Base, open_browser

login_url = 'http://localhost:8082/ecshop/user.php'


class LoginPage(Base):
    """封装页面表现层,制作页面元素的定位器"""
    username_loc = ('name', 'username')  # 用户名输入
    password_loc = ('name', 'password')  # 密码输入
    remember_loc = ('id', 'remember')  # 记住密码
    submit_loc = ('class name', 'us_Submit')  # 立即登录
    question_loc = ('link text', '密码问题')  # 找回密码_密码问题
    email_loc = ('link text', '邮件')  # 找回密码_邮件
    message_loc = ('link text', '短信验证')  # 找回密码_短信验证
    register_loc = ('css selector', '.usTxt > a > img')  # 立即注册
    result_loc = ('class name', 'f4_b')  # 左上角定位
    """封装操作层:对表现元素的操作"""

    def input_username(self, username):
        """
        输入用户名
        :param username:用户名
        :return:
        """
        self.send_keys(text=username, locator=self.username_loc)

    def input_password(self, password):
        """
        输入密码
        :param password:密码
        :return:
        """
        self.send_keys(text=password, locator=self.password_loc)

    def remember_password(self):
        """
        点击记住密码
        :return:
        """
        self.click(locator=self.remember_loc)

    def click_submit(self):
        """
        点击立即登录
        :return:
        """
        self.click(locator=self.submit_loc)

    def find_password_by_question(self):
        """
        点击密码问题找回密码
        :return:
        """
        self.click(locator=self.question_loc)

    def find_password_by_message(self):
        """
        点击找回密码_短信验证
        :return:
        """
        self.click(locator=self.message_loc)

    def find_password_by_mail(self):
        """
        点击找回密码_邮件
        :return:
        """
        self.click(locator=self.message_loc)

    def click_register(self):
        """
        点击立即注册
        :return:
        """
        self.click(locator=self.register_loc)

    def is_login_success(self, username):
        """
        判断是否登录成功
        :param username:
        :return:
        需要一个判断元素文本是否和给定的文本一致
        """



if __name__ == '__main__':
    from time import sleep

    driver = open_browser()
    login = LoginPage(driver)
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
    # 5.点击立即注册
    # # login.click_register()
    # 6.点击邮箱找回
    # login.find_password_by_mail()
    # 7.点击短信找回
    # login.find_password_by_message()
    # 8.点击问题找回
    login.find_password_by_question()
    sleep(5)
    # 5.关闭浏览器
    login.close_browser()
