import allure


def test_aaa():
    print('aaaa')
    assert 1


@allure.step(title="测试登录的流程")
def test_login():
    allure.attach('登录', '输入用户名')
    print("aaaa") #找用户名
    allure.attach('登录', '输入密码')
    print("bbbb") #找密码
    allure.attach('登录', '点击登录')
    print("aaaa") #点击登录
    assert 1