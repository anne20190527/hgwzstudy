from appium_po.xueqiu_po import BasePage


class SearchPage(BasePage):
    def search(self, keyword):
        self.driver.find_element_by_id("search_input_text").send_keys(keyword)
        return self

    def select(self,index):
        self.driver.find_elements_by_id("name")[index].click()
        return self

    def get_name(self):
        return self.driver.page_source