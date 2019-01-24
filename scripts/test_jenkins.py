import allure


def test_aaa():
    print('aaaa')
    assert 1


@allure.step(title="测试步骤001")
def test_bbb():
    allure.attach('描述', '我是测试步骤001的描述～～～')
    print('bbb')
    print('bbb')

    print('bbb')
    assert 1