from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

#伊思听说有个很cool的在线待办事项应用
#她去看了这个应用的首页
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get("http://localhost:8000")

#她注意到网页的标题和开头都包括"To-Do"这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == "__main__":
    unittest.main(warning = "ignore")
#应用邀请他输入一个待办事项
#他输入buy peacock feathers
#伊思的爱好是使用假蝇做饵钓鱼
#她按回车键后页面更新
#待办事项显示了1：buy。。。
#页面又显示了一个文本框可以输入其他待办事项
#他输入了use peacock feathers to make a fly
#伊思做事很有条理
#页面再次更新，它的清单中显示了这两个待办事项
#伊思想知道这个网站是否会记住它的清单
#她看到网站为她生成了一个唯一的url
#而且页面中由一些文字生成解说这个功能
#他访问那个url发现它的待办事项列表还在
# 她很满意，去睡觉了
