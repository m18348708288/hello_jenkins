import os,sys
sys.path.append(os.getcwd())
import page
import time
from page.navigation_page import NavigationPage
from base.init_driver import get_driver
class TestLogin:
    #在测试函数之前执行
    def setup_class(self):
        #1.初始化driver
        self.driver = get_driver(page.aolai_app_package,page.aolai_app_activity)
        #2.初始化导航类
        self.navigation_page = NavigationPage(self.driver)

    #最后执行
    def teardown_class(self):
         #关闭driver
         self.driver.quit()

    #测试函数
    def test_login(self):
        #1.点击我的
        self.navigation_page.get_home_page_obj().click_btn_my()
        #2.点击已有账号 去登录
        self.navigation_page.get_regist_page_obj().click_btn_already_account()
        #3 输入账号密码 登录
        self.navigation_page.get_login_page_obj().click_btn_login("13488834010","159357li")
        #4.跳转到个人中心 点击个人中心的左上角的设置按钮
        time.sleep(2)
        self.navigation_page.get_person_center_obj().click_btn_left_setting()
        #5.实现滑动 点击退出 在点击确认对话框
        self.navigation_page.get_setting_page_obj().click_setting_btn_logout()


