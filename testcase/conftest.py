import pytest

@pytest.fixture(scope='session')
def f():
    #前置操作
    print('用例执行开始了')

    #给用例传递内容
    yield '来自fixture的数据'

    #后置操作
    print('用例执行结束了')