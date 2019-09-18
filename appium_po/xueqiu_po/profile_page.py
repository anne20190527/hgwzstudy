from appium_po.xueqiu_po import BasePage


class ProfilePage(BasePage):
    def login_by_phone(self, phone, code):
        self.driver.find_element_by_id("iv_login_phone").click()
        self.driver.find_element_by_id("register_phone_number").send_keys(phone)
        self.driver.find_element_by_id("register_code").send_keys(code)
        self.driver.find_element_by_id("button_next").click()
        return self

    def get_msg(self):
        message = self.driver.find_element_by_id("md_content").text
        return message

    def login_by_wx(self):
        pass

    def login_by_weibo(self):
        pass

    def login_by_qq(self):
        pass
