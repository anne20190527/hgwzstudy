from appium.webdriver.common.touch_action import TouchAction
from appium_po.xueqiu_po import BasePage
from appium_po.xueqiu_po import SearchPage


class Optional(BasePage):
    def search(self):
        self.driver.find_element_by_id("action_search").click()
        return SearchPage(self.driver)

    def add_stock(self):
        self.driver.find_element_by_id("follow_btn").click()# 加自选
        if "下次再说" in self.driver.page_source:
            self.driver.find_element_by_id("md_buttonDefaultNegative").click()
        else:
            pass
        return self

    def delete_stock(self):
        stock1 = self.driver.find_element_by_xpath("//*[contains(@text, '小米集团-W')]")
        TouchAction(self.driver).long_press(stock1, 1000).perform()
        self.driver.find_element_by_xpath("//*[contains(@resource-id, 'md_title') and @text='删除']").click()
        return self

    def get_stockstatus(self, isfollow=True):
        if isfollow:
            ele = self.driver.find_element_by_id("follow_btn")
        else:
            ele = self.driver.find_element_by_id("followed_btn")
        if ele:
            return ele.text
        else:
            return None

    def cancel(self):
        self.driver.find_element_by_id("action_close").click()
        return self