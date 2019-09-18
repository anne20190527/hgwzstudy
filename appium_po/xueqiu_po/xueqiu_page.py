from appium.webdriver.common.touch_action import TouchAction
from appium_po.xueqiu_po import BasePage
from appium_po.xueqiu_po.driver import Driver
from appium_po.xueqiu_po.profile_page import ProfilePage
from appium_po.xueqiu_po import SearchPage
from appium_po.xueqiu_po.optional import Optional


class XueqiuPage(BasePage):
    def __init__(self):
        self.driver = Driver().get_driver()

    def goto_search(self):
        self.driver.find_element_by_id("home_search").click()
        return SearchPage(self.driver)

    def goto_profile(self):
        self.driver.find_element_by_id("user_profile_icon").click()
        return ProfilePage(self.driver)

    def goto_zixuan(self):
        self.driver.find_element_by_xpath("//*[contains(@text, '自选')]").click()
        if "新增手势" in self.driver.page_source:
            location = self.driver.get_window_size()
            width = location['width']
            height = location['height']
            TouchAction(self.driver).press(x=int(0.5*width), y=int(0.5*height)).perform()#去掉新增手势提示
        else:
            pass
        return Optional(self.driver)

    def goto_optional(self):
        return Optional(self.driver)
