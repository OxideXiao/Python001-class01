import time
import requests

#from fake_useragent import UserAgent

#ua = UserAgent(verify_ssl=False)
headers = {
'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
'Referer' : 'https://shimo.im/login?from=home',
'Host': 'shimo.im',
'Origin': 'https://shimo.im',
'x-requested-with': 'XmlHttpRequest',
'x-source': 'lizard-desktop',
}

session1 = requests.Session()

login_url = 'https://shimo.im/lizard-api/auth/password/login'
form_data = {
'email':'********@sina.com', #自己的邮箱
'mobile': '+86undefined',
'password': '********',  #密码
}

# post数据前获取cookie
pre_login = 'https://shimo.im/welcome'
pre_resp = session1.get(pre_login, headers=headers)

response = session1.post(login_url, data=form_data, headers=headers, cookies=session1.cookies)
print(response,':',response.text)

time.sleep(2)

# 登陆后请求工作台信息
url_workplace = 'https://shimo.im/lizard-api/files?type=used&collaboratorCount=true&collaboratorCount&limit=100&lastTimestamp=1593968167647'
response2 = session1.get(url_workplace, headers = headers, cookies = session1.cookies)

print('==========工作台信息=========')
print(response2.text)
