from appium_po.xueqiu_po.xueqiu_page import XueqiuPage


class TestProfile:
    def setup_class(self):
        self.xueqiu = XueqiuPage()
        self.profile = self.xueqiu.goto_profile()

    def test_login_by_phone(self):
        assert "验证码已过期" == self.profile.login_by_phone("1234567891", "1234").get_msg()