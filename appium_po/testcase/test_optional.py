from appium_po.xueqiu_po.xueqiu_page import XueqiuPage


class TestOptional:
    def setup_class(self):
        self.xueqiu = XueqiuPage()
        self.zixuan = self.xueqiu.goto_zixuan()
        self.optional = self.xueqiu.goto_optional()

    def test_add(self):
        self.zixuan.search().search("xiaomi").select(0)
        self.optional.add_stock()
        self.optional.cancel()
        self.optional.search().search("xiaomi").select(0)
        assert self.optional.get_stockstatus(False) == "已添加"
        self.optional.cancel()

    def test_delete(self):
        self.zixuan.delete_stock()
        self.optional.search().search("xiaomi").select(0)
        assert self.optional.get_stockstatus() == "加自选"
