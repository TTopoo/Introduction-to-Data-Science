import requests

proxy='218.60.8.99:3129'  #本地代理
proxies={
    'http':'http://'+proxy,
}
try:
    response=requests.get('http://httpbin.org/get',proxies=proxies)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('错误:',e.args)