import requests
import jsonpath

#0. 创建会话，共享参数和网络链接
s = requests.Session()

#1. 登录
resp = s.request(
    "post",
    "http://api.fbi.com:9225/rest-v2/login/access_token",
    json={
        "email": "bf@qq.com",
        "password": 'bf123456'
    }
)

if resp.status_code == 200:
    print('成功')
else:
    print('失败')

# 提取token，共享参数
token = jsonpath.jsonpath(resp.json(),'$.access_token')[0]
s.headers.update({"Authorization": f"Bearer {token}"})

total = resp.json()['total']

#2. 新增任务
resp = s.request(
    "post",
    "http://api.fbi.com:9225/rest-v2/todo",
    json={
        "title": "新的任务",
        "is_done": False
    }
)

if resp.status_code == 200:
    print('成功')

# 提取新增任务的id，用于关联
new_id = jsonpath.jsonpath(resp.json(),'$.id')[0]

#3. 查询任务列表
resp = s.request(
    "get",
    "http://api.fbi.com:9225/rest-v2/todo",
)

if resp.status_code == 200:
    print('成功')

newtotal = resp.json()['total']

if newtotal == total + 1:
    print('成功')

#4. 删除任务
resp = s.request(
    "get",
    f"http://api.fbi.com:9225/rest-v2/todo/{new_id}",
)

renewtotal = resp.json()['total']


if resp.status_code == 200:
    print('成功')

if renewtotal == newtotal - 1:
    print('成功')

if renewtotal == total:
    print('成功')