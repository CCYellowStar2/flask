from flask import Flask, request, redirect
import requests

app = Flask(__name__)

def get_location_info_from_ip2location(api_key, ip_address):
    url = f"https://api.ip2location.io/?key={api_key}&ip={ip_address}"
    response = requests.get(url)
    data = response.json()
    return data

@app.route('/1')
def redirect_based_on_location():
    user_ip = request.remote_addr  # 获取用户的 IP 地址
    api_key = "2C4BFA3DFA445146D966BB3927CD4D87"  # 替换成你的IP2Location API密钥

    location_info = get_location_info_from_ip2location(api_key, user_ip)
    
    if location_info["country_code"] == "CN":
        new_url = 'http://123.ccyacg.xyz' + request.full_path  # 拼接国内用户的新链接
        return redirect(new_url, code=302)  # 302 重定向
    else:
        new_url = 'http://pan.ccyacg.xyz' + request.full_path  # 拼接国外用户的新链接
        return redirect(new_url, code=302)  # 302 重定向
