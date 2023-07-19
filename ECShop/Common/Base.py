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
import os

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def open_browser(browser: str = 'chrome'):
    """
    打开浏览器
    :param browser: 浏览器名称   browser: str 指定数据类型
    :return: driver
    """
    if browser.lower() == 'chrome':  # 打开谷歌浏览器
        option = webdriver.ChromeOptions()
        chromedriver = os.path.join(os.getcwd(), 'chromedriver_windows')
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
        option.add_argument('--disable-blink-features=AutomationControlled')
        return webdriver.Chrome(chromedriver, options=option)
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

    def open_url(self, url):
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
                sleep(1)
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
        :param locator:定位器
        :param timeout: 超时器
        :return:
        """
        try:
            element = self.find_element(locator=locator, timeout=timeout)
            return element.text
        except:
            print('获取文本失败')
            return False

    def get_element_value_text(self, locator: tuple, timeout: int = 10):
        """

        :param locator:定位器
        :param timeout: 超时时间
        :return: value_text
        """
        try:
            element = self.find_element(locator=locator, timeout=timeout)
            return element.get_attribute('value')
        except:
            print('value属性值获取失败')
            return False

    def close_browser(self):
        """
        关闭浏览器
        :return:
        """
        self.driver.quit()

    def is_text_in_element(self, text, locator, timeout=10):
        """
        判断给定的文本是否和元素的文本相同,
        如果相同返回True,反之返回False
        :return:
        """
        try:
            element = self.find_element(locator=locator, timeout=timeout)
            result_text = element.text
            if result_text == text:  # 判断元素文本是否相同
                return result_text == text
            else:
                return False
        except:
            print(f'元素{locator}没有找到')
            return False  # 元素没找到情况下

    def click_checkbox(self, locator: tuple, timeout: int = 10):
        """
        复选框点击
        :param locator: 定位器
        :param timeout: 超时时间
        :return:
        """
        try:
            if self.find_element(locator=locator, timeout=timeout).is_selected():
                pass
            else:
                self.click(locator=locator, timeout=timeout)
        except:
            print(f'元素{locator}不存在,无法点击')

    def select_pull_down_element(self, locator, index: int = 0, timeout: int = 10):
        """
        下拉菜单选择
        :param locator:
        :param index:
        :return:
        """
        try:
            element = self.find_element(locator=locator, timeout=timeout)
            element = Select(element)
            element.select_by_index(index)
        except:
            print(f'元素{locator}不存在,无法选择')

    def click_iframe(self, locator_iframe: tuple, locator: tuple, timeout: int = 10):
        """
        进入frame,点击元素
        :param locator_frame:frame
        :param locator: 元素定位器
        :param timeout:
        :return:
        """
        try:
            frame = self.find_element(locator=locator_iframe)
            self.driver.switch_to.frame(frame)
            element = self.find_element(locator=locator, timeout=timeout)
            element.click()
            self.driver.switch_to.default_content()
        except:
            print(f'{locator_iframe}或者元素{locator}不存在,无法选择')

    def send_keys_iframe(self, locator_iframe: tuple, locator: tuple, text, timeout: int = 10):
        """
        进入frame,选择元素,输入
        :param locator_frame: frame
        :param locator: 元素定位器
        :param text: 输入内容
        :param timeout:
        :return:
        """
        try:
            frame = self.find_element(locator=locator_iframe)
            self.driver.switch_to.frame(frame)
            element = self.find_element(locator=locator, timeout=timeout)
            element.clear()  # 先清空
            element.send_keys(text)  # 再输入
            self.driver.switch_to.default_content()
        except:
            print(f'{locator_iframe}或者元素{locator}不存在,无法输入')

    def enter_iframe(self, locator: tuple):
        """
        进入frame,选择元素,输入
        :param locator_frame: frame
        :param locator: 元素定位器
        :param text: 输入内容
        :param timeout:
        :return:
        """
        frame = self.find_element(locator=locator)
        self.driver.switch_to.frame(frame)

    def quit_iframe(self):
        """
        退出iframe
        :return:
        """
        self.driver.switch_to.default_content()

    def send_keys_data(self, locator, id, text, timeout: int = 10):
        """
        输入
        :param locator: 定位器
        :param text: 输入内容
        :param timeout: 超时
        :return:
        """
        try:
            js = f'document.getElementById("{id}").removeAttribute("readonly");'
            self.driver.execute_script(js)
            element = self.find_element(locator=locator, timeout=timeout)
            element.clear()  # 先清空
            element.send_keys(text)  # 再输入
        except:
            print(f'元素{locator}不存在,无法输入')

    def back(self):
        """
        后退
        :return:
        """
        self.driver.back()

    def remove_alerta_window(self, id):
        """
        去除指定ID弹窗
        :param id:
        :return:
        """
        js = f'document.getElementById("{id}").style.display="none";'
        self.driver.execute_script(js)


if __name__ == '__main__':
    import time

    driver = open_browser()  # 打开浏览器
    base = Base(driver)
    base.open_url('http://www.baidu.com/')
    search_loc = ('id', 'kw')
    # 百度按钮定位器
    button_loc = ('id', 'su')
    # 设置定位器
    settings_loc = ('id', 's-usersetting-top')
    # 获取设置text值
    print(base.get_element_text(settings_loc))
    # 获取百度按钮的value属性值
    print(base.get_element_value_text(button_loc))
    # 输入文字'PO设计模式'
    base.send_keys(locator=search_loc, text='PO设计模式')
    # 点击百度按钮
    base.click(locator=button_loc)
    time.sleep(5)
    base.close_browser()
