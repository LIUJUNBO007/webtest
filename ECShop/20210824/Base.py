"""
文件名: Base.py]
作用: 对selenium进行二次封装
    1.打开浏览器
    2.打开网址
    3.元素定位
    4.元素操作
    5.元素属性获取
    ....

"""
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_browser(browser: str = 'chrome'):
    """
    打开浏览器
    :param browser: 浏览器名称   browser: str 指定数据类型
    :return: driver
    """
    if browser.lower() == 'chrome':  # 打开谷歌浏览器
        return webdriver.Chrome()
    elif browser.lower() == 'firefox':  # 打开火狐浏览器
        return webdriver.Firefox()
    elif browser.lower() == 'edge':  # 打开Edge浏览器
        return webdriver.Edge()
    else:
        print('选择正确的浏览器,例如: Chrome,Firefox,Edge')


class Base(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()  # 浏览器窗口最大化

    def open_url(self, url: str):
        """
        打开网址
        :param url: 网址
        :return:
        """
        try:
            self.driver.get(url)
        except:
            print(f'地址{url}格式错误')

    def find_element(self, locator: tuple, timeout: int = 10):
        """
        元素定位,定位单个元素,如果元素存在,返回元素本身,反之返回False
        :param locator: 定位器,数据类型,元组;('元素定位方法','方法对应的值')
        :param timeout: 超时时间
        :return: element
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except:
            print(f'元素{locator}没找到')
            return False

    def find_elements(self, locator: tuple, timeout: int = 10):
        """
        元素定位,复数形式,如果元素存在,返回元素列表,反之,返回False
        :param locator: 定位器
        :param timeout: 超时时间
        :return: list
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        except:
            print(f'元素{locator}没找到')
            return False

    def click(self, locator: tuple, timeout: int = 10):
        """
        点击
        :param locator: 定位器
        :param timeout: 超时时间
        :return:
        """
        try:
            element = self.find_element(locator=locator, timeout=timeout)
            element.click()
        except:
            print(f'元素{locator}不存在,无法点击')

    def clicks(self, locator: tuple, timeout: int = 10):
        """
        点击
        :param locator: 定位器
        :param timeout: 超时时间
        :return:
        """
        try:
            elements = self.find_elements(locator=locator, timeout=timeout)
            for element in elements:
                element.click()
        except:
            print(f'元素{locator}不存在,无法点击')

    def send_keys(self, text, locator: tuple, timeout: int = 10):
        """
        输入
        :param locator: 定位器
        :param text: 输入内容
        :param timeout: 超时
        :return:
        """
        try:
            element = self.find_element(locator=locator, timeout=timeout)
            element.clear()  # 先清空
            element.send_keys(text)  # 再输入
        except:
            print(f'元素{locator}不存在,无法输入')

    def get_element_text(self, locator: tuple, timeout: int = 10):
        """
        获取元素的文本值,如果存在,返回文本,反之返回False
        :param locator: 定位器
        :param timeout: 超时时间
        :return: element_text
        """
        try:
            element = self.find_element(locator=locator, timeout=timeout)
            return element.text  # 返回文本值
        except:
            print('获取文本失败')
            return False

    def get_element_value_text(self, locator: tuple, timeout: int = 10):
        """
        获取元素的value属性值,如果存在,返回value值,反之,返回False
        :param locator: 定位器
        :param timeout: 超时时间
        :return: value_text
        """
        try:
            element = self.find_element(locator=locator, timeout=timeout)
            return element.get_attribute('value')  # 获取value属性值
        except:
            print('value属性值获取失败')
            return False

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()


if __name__ == '__main__':
    import time

    driver = open_browser()  # 打开浏览器
    base = Base(driver)
    base.open_url('http://www.baidu.com/')  # 输入网址
    # 百度首页输入框定位器
    search_loc = ('id', 'kw')
    # 百度按钮定位器
    button_loc = ('id', 'su')
    # 设置定位器
    settings_loc = ('id', 's-usersetting-top')
    # 获取设置text值
    print(base.get_element_text(search_loc))
    # 获取百度按钮的value属性值
    print(base.get_element_value_text(search_loc))
    # 输入文字'PO设计模式'
    # base.send_keys(locator=search_loc, text='PO设计模式')
    # 点击百度按钮
    # base.click(locator=button_loc)
    time.sleep(5)
    base.close_browser()
