from Common.Base import Base, open_browser

regiser_url = 'http://localhost:8082/ecshop/user.php?act=register'


class RegisterPage(Base):
    username_loc = ('name', 'username')  # 用户名输入
    email_loc = ('name', 'email')  # 邮箱输入
    password_loc = ('name', 'password')  # 密码输入
    conform_password_loc = ('id', 'conform_password')  # 确认密码
    qq_loc = ('name', 'extend_field2')  # 输入QQ
    office_phone_loc = ('name', 'extend_field3')  # 输入办公室电话
    home_phone_loc = ('name', 'extend_field4')  # 输入家庭电话
    mobilephone_loc = ('name', 'extend_field5')  # 输入手机号码
    password_question_loc = ('name', 'sel_question')  # 密码问题选择
    passwd_answer_loc = ('name', 'passwd_answer')  # 密码问题答案输入
    agreement_loc = ('name', 'agreement')  # 协议同意按钮
    user_agreement_loc = ('link text', '用户协议')  # 用户协议
    submit_loc = ('name', 'Submit')
    switch_login_link_loc = ('link text', '我已有账号，我要登录')
    forget_password_link_loc = ('link text', '您忘记密码了吗？?')
    index_loc = ('name', 'sel_question')
    is_register_success_loc = ('class name', 'f4_b')

    def input_username(self, username):
        self.send_keys(text=username, locator=self.username_loc)

    def input_email(self, email):
        self.send_keys(text=email, locator=self.email_loc)

    def input_password(self, password):
        self.send_keys(text=password, locator=self.password_loc)

    def input_conform_password(self, password):
        self.send_keys(text=password, locator=self.conform_password_loc)

    def input_qq(self, qq):
        self.send_keys(text=qq, locator=self.qq_loc)

    def input_office_phone(self, officephone):
        self.send_keys(text=officephone, locator=self.office_phone_loc)

    def input_home_phone(self, homephone):
        self.send_keys(text=homephone, locator=self.home_phone_loc)

    def input_mobilephone(self, mobilephone):
        self.send_keys(text=mobilephone, locator=self.mobilephone_loc)

    def input_passwd_answer(self, passwdanswer):
        self.send_keys(text=passwdanswer, locator=self.passwd_answer_loc)

    def click_agreement(self):
        # if self.find_element(locator=self.agreement_loc).is_selected():
        #     pass
        # else:
        #     self.click(locator=self.agreement_loc)
        self.click_checkbox(locator=self.agreement_loc)

    def click_user_agreement(self):
        self.click(locator=self.user_agreement_loc)

    def search_passwd_question(self, index):
        self.select_pull_down_element(locator=self.index_loc, index=index)

    def click_submit(self):
        self.click(locator=self.submit_loc)

    def click_switch_login_link(self):
        self.click(locator=self.switch_login_link_loc)

    def click_forget_password_link(self):
        self.click(locator=self.forget_password_link_loc)

    def is_register_success(self, username):
        return self.is_text_in_element(text=username, locator=self.is_register_success_loc)
