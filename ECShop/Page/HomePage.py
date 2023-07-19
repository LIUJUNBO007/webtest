"""
作用:对登录页面进行封装
封装内容:页面的表现曾和操作层
Page类:继承Base类


"""

from Common.Base import Base, open_browser
from Page.BackStageLoginPage import BackStageLoginPage
from time import sleep
import concurrent.futures
from random import randint

login_url = 'http://www.brainbestadvent.com/zh-CN'


# login_url = 'http://taotan.front.test.cdtaotan.com/appraisal/31883f04f90d?hl=CN'

class HomePage(Base):
    start_test_loc = ("css selector", "div.banner_content_ingda > div > a > div")
    answer_loc = ("css selector", f"div.answers_box_content > div.answers_box > div:nth-child({randint(1, 6)})")
    get_result_loc = ("css selector", "div:nth-child(2) > button > div")
    name_loc = ("name", "username")
    country_sex_loc = ("css selector", "div:nth-child(2) > select > option:nth-child(1)")
    birth_year_loc = ('css selector', 'div.item_input_label.one_hsds > select > option:nth-child(2)')
    mail_loc = ("name", "email")
    commit_loc = ("css selector", "#information > div.input_box > button")

    def click_start_test(self):
        self.click(locator=self.start_test_loc)

    def clicks_answer(self):
        self.clicks(locator=self.answer_loc)

    def click_get_result(self):
        self.click(locator=self.get_result_loc)

    def send_name(self, keys):
        self.send_keys(locator=self.name_loc, text=keys)

    def clicks_country_sex(self):
        self.click(locator=self.country_sex_loc)

    def click_birth_year(self):
        self.click(locator=self.birth_year_loc)

    def send_email(self, keys):
        self.send_keys(locator=self.mail_loc, text=keys)

    def click_commit(self):
        self.click(locator=self.commit_loc)


if __name__ == '__main__':
    def task():
        driver = open_browser()  # 打开浏览器
        login = HomePage(driver)
        login.open_url(login_url)
        login.click_start_test()
        sleep(1)
        login.clicks_answer()
        sleep(1)
        login.click_get_result()
        sleep(1)
        login.send_name("TTEST")
        login.click_birth_year()
        login.clicks_country_sex()
        login.send_email("awrenceruckery@gmail.com")
        login.click_commit()
        sleep(10)
        return f"完成测试{randint(0, 5)}"


    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # 提交任务到线程池
        futures = [executor.submit(task) for i in range(0, 5)]
        print(f"Task number:", len(futures))
        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                print(f"Task result: {result}")
            except Exception as e:
                print(f"Task encountered an exception: {e}")
