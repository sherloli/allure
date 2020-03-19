import pytest
import allure
import time

@allure.epic("xx项目")
@allure.issue("http://xxx/zentao/bug-view-1.html")  # 禅道bug地址
@allure.testcase("http://xxx/zentao/testcase-view-5-1.html")  # 禅道用例连接地址
@allure.feature("第一个Demo测试")
class TestDemo():

    @allure.story("用例1")
    @allure.step("先打印1，在 打印2")
    @allure.severity("minor")
    def test_1(self,log_demo):

        time.sleep(1)
        print("1")
        assert 1==2

    @allure.story("用例2")
    @allure.description("描述用例2")
    @allure.severity("blocker")
    def test_2(self,log_demo):
        time.sleep(2)
        print("2")

    @allure.story("用例3")
    @allure.description("描述用例3")
    @allure.severity("critical")
    def test_3(self, log_demo):
        time.sleep(3)
        print("3")
        with open(r"C:\Users\cola\Desktop\2.png","rb") as f:
            context=f.read()
            allure.attach(context,"错误截图",attachment_type=allure.attachment_type.PNG)
        assert 1==2

    @allure.story("用例4")
    @allure.description("描述用例4")
    @allure.severity("blocker")
    #@pytest.mark.skip(reason="你不管嘛")
    def test_4(self, log_demo):
        time.sleep(4)
        print("4")
        assert 1 == 2

if __name__ == '__main__':
    pytest.main(["-s","test_demo.py"])