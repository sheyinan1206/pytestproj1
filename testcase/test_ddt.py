import pytest
import requests

def add(a, b):
    return a + b

@pytest.mark.parametrize("a, b", [(1, 2), (3, 4), ("a", "b"), (["a"], [4])],)
def test_add(a, b):
    c = a + b
    assert c == a + b


@pytest.mark.parametrize(
        ["accounts", "pwd", "code"], 
        [["admin", "123456", "200"], 
         ["admin", "123456789", "0"],
         ["admin", "", "1"]]
                         )
def test_login(accounts, pwd, code):
    s = requests.Session()
    method = 'post'
    url = 'http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html'
    json = {
        'accounts': accounts,
        'pwd': pwd
    }
    resp = s.request(method,url,json=json)
    assert resp.status_code == int(code)