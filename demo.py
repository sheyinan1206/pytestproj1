import requests
import jsonpath

s = requests.Session()

method = 'post'

url = 'http://shop-xo.hctestedu.com/index.php?s=/index/user/logininfo.html'

# url ='https://www.baidu.com'

json = {
    'accounts': 'admin',
    'pwd': '123456'

}

resp = s.request(method,url,json=json)

# assert resp.status_code == 200

print("行：",resp.status_code,resp.reason)
print("头：",resp.headers,)
print("头：",dict(resp.cookies),)

print("状态码：", resp.status_code)
print("响应内容：", resp.text)  # 先查看响应内容是什么

# 只有确认响应是JSON才解析
if resp.status_code == 200 and resp.text.strip():
    try:
        data = resp.json()
        print("解析的JSON数据：", data)
        # 注意：正确的字段名是 access_token（不是 accesss_token）
        token = jsonpath.jsonpath(data, '$.access_token')[0]
        s.headers.update({"Authorization": token})
        print(s.headers)
    except Exception as e:
        print("JSON解析失败：", e)
else:
    print("响应为空或状态码异常")

# print(resp.json()['token_type'])

# print(resp.content ) #二进制：传输
# print(resp.text ) #文本：阅读
# print(resp.json() ) #字典：使用

# 共享参数（全局凭据session）
# token = resp.json()['accesss_token'] #数据的提取（字典）

#其他提取方式：re、jsonpath

token = jsonpath.jsonpath(resp.json(),'$.accesss_token')[0]

s.header.update({"Authorization": f"Bearer {token}"})

print(s.headers)