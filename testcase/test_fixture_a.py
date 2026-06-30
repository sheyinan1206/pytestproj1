import pytest

# @pytest.fixture(scope='session')
# def f():
#     #前置操作
#     print('用例执行开始了')

#     #给用例传递内容
#     yield '来自fixture的数据'

#     #后置操作
#     print('用例执行结束了')

#通过标记调用
@pytest.mark.usefixtures('f')
def test_abc(f):
    print(f)

#通过参数调用
def test_123(f):
    print(f)