import pytest
from appium_po.xueqiu_po.xueqiu_page import XueqiuPage


class TestSearch:
    def setup_class(self):
        self.xueqiu = XueqiuPage()

    @pytest.mark.parametrize("keyword, name",
                         [("alibaba", "阿里巴巴"),
                          ("xiaomi", "小米"),
                          ("google", "谷歌")])
    def test_search(self, keyword, name):
        assert name in self.xueqiu.goto_search().search(keyword).select(0).get_name()
        self.xueqiu.goto_optional().cancel()


