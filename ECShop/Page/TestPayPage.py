from Common.Base import Base, open_browser
from Page.BackStageLoginPage import BackStageLoginPage
from time import sleep
import concurrent.futures
from random import randint
from Common.Database import Database

# login_url = 'https://taotan.front.test.cdtaotan.com/landing_page/yellow_boy/IIQQ-1511?hl=EN'
# login_url = 'http://front.minsynaesthesia.com/landing_page/yellow_boy/1511'
login_url = 'https://www.brainbestadvent.com/landing_page/yellow_boy/IQB-1516?hl=EN'

class TestPayPage(Base):
    start_test_loc = ("css selector", "div.home_page_banner_box_content > div > button")
    answer_loc = ("css selector", "div.answers>div:nth-child(6)")
    get_result_loc = ("css selector", "div:nth-child(2) > button > div")
    name_loc = ("css selector", ".el-input__wrapper>[placeholder='Please enter your name']")
    mail_loc = ("css selector", ".el-input__wrapper>[placeholder='Please enter an email address']")
    submit_loc = ("css selector", "#information > div > div.information_box_form > button")
    # 支付方案选择
    # pay_loc = ("css selector", "div:nth-child(3) > div.scheme_page_box_scheme_list_item_button")
    pay_loc = ("css selector", "div > div.scheme_page_box_scheme_list_item_button")
    card_nu_loc = ("css selector", "div > input[placeholder='Card number']")
    card_date_loc = ("css selector", "div > input[placeholder='MM / YY']")
    card_code_loc = ("css selector", "div > input[placeholder='XXX']")
    pay_commit_loc = ("css selector", "div.payment_frame_buttons > button > div")

    def click_start_test(self):
        self.click(locator=self.start_test_loc)

    def click_answer(self):
        self.click(locator=self.answer_loc)

    def click_result(self):
        self.click(locator=self.get_result_loc)

    def send_name(self, keys):
        self.send_keys(locator=self.name_loc, text=keys)

    def send_email(self, keys):
        self.send_keys(locator=self.mail_loc, text=keys)

    def click_submit(self):
        self.click(locator=self.submit_loc)

    def click_pay(self):
        self.click(locator=self.pay_loc)

    def send_card_nu(self, keys):
        self.send_keys(locator=self.card_nu_loc, text=keys, timeout=30)

    def send_card_date(self, keys):
        self.send_keys(locator=self.card_date_loc, text=keys, timeout=30)

    def send_card_code(self, keys):
        self.send_keys(locator=self.card_code_loc, text=keys, timeout=30)

    def click_pay_commit(self):
        self.click(locator=self.pay_commit_loc)


if __name__ == '__main__':
    def task():
        driver = open_browser()  # 打开浏览器
        login = TestPayPage(driver)
        login.open_url(login_url)
        login.click_start_test()

        for i in range(60):
            login.click_answer()
            # sleep(0.1)
        sleep(2)
        # login.click_result()
        # sleep(5)
        # login.send_name(keys="llljjjb")
        # login.send_email(keys="343176631@qq.com")
        # login.send_email(keys="1255177725@qq.com")
        # login.click_submit()
        # login.click_pay()
        # sleep(10)
        # login.enter_iframe(locator=("css selector", "#custom_card_number > iframe"))
        # login.send_card_nu(keys='4012000300000021')
        # login.quit_iframe()
        # sleep(2)
        # login.enter_iframe(locator=("css selector", " #custom_expiry > iframe"))
        # login.send_card_date(keys='0723')
        # login.quit_iframe()
        # sleep(2)
        # login.enter_iframe(locator=("css selector", " #custom_cvc > iframe"))
        # login.send_card_code(keys='123')
        # login.quit_iframe()
        #
        # # login.click_pay_commit()
        # sleep(3)
        # # login.click_pay_commit()
        sleep(5000)


    # db = Database()
    # sql = 'select count(1) from t_exam_order where pay_status=10;'
    # result1 = db.readone(sql=sql)['count(1)']
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
    # sql = 'select count(1) from t_exam_order where pay_status=10;'
    # result2 = db.readone(sql=sql)['count(1)']
    #
    # result_nu = result2 - result1
    # print(result1, result2, result_nu)
