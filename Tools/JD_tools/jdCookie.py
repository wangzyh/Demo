import requests
import json
import time
import os
import re
import notification

"""
1、抓包，登录 https://bean.m.jd.com 点击签到并且出现签到日历后
2、返回抓包，搜索关键词 functionId=signBean 复制Cookie中的pt_key与pt_pin
       电脑获取cookie可以参考 https://ruicky.me/2020/07/18/jd-cookie/
3、注意，cookies会过期,大约为一个月
4、python3.6+ 环境，需要requests包
集中cookie管理
多账号准备
过期检查
需要推送通知的，修改notification.py
"""

###############################
# 方案1 本地执行、云服务器、云函数等等   下载到本地，填写参数，执行
# __jdu=16023462707861144776600; cud=07b55c1f28b97b8bc8a314fbfe858b2a; shshshfpa=9f96f31d-915b-c13b-7f04-a65fc40747b5-1602346274; shshshfpb=qpe%2FmrmFnImldWvQduOMhUg%3D%3D; pinId=yQv0zFDUZXuYSigmPgKw1g; unick=%E5%A5%BD%E7%94%B7%E9%93%B6%E4%B8%8D%E6%AD%A2%E6%9B%BE%E5%B0%8F%E8%B4%A4; _tp=K6P%2F%2BloT%2FGTAYXp7glEj0A%3D%3D; _pst=13693739645_p; user-key=c86303d4-da7d-4c57-912c-176f6c968141; ipLocation=%u4e0a%u6d77; pin=13693739645_p; areaId=2; ipLoc-djd=2-2825-51931-0; ceshi3.com=201; cn=7; PCSYCityID=CN_310000_310100_0; unpl=V2_ZzNtbUJWFxMgXxNdfx0IDGJTG1kSBEFFfAtDU3JMXFFjA0FVclRCFnUUR1ZnGlwUZwcZWUNcQBZFCEdkexhdBGYKGlRKVXMVcQ8oVRUZVQAJbUIPQwUXESUNT1N6H1oENAIibUFXcxRFCEFVeBtZAmQFE1tLUEMVcA1AUnweXQRXMxJVRmdDFHQLRFx%2fGlkCbwMWWnKA6rujhOCAwrOLt%2bUzFltBUUcUdAlFZHopXTUmbRJcRlJHHHQPC1R8GF8HYgQRW0NRShJ1CENRfR9bAmYCIlxyVA%3d%3d; __jdv=122270672|www.linkstars.com|t_1000089893_156_0_184__ac0ce5a4860770b0|tuiguang|10e7dfd855e84a85ab3a82468d1e51b9|1616313022995; cvt=71; shshshfp=985122c1f8c3518d1b580532196eaaa1; shshshsID=cc1e614230e8706363d42bb5416affc2_4_1616504982991; csn=4; wlfstk_smdl=t543wrsy496j5ip6mjd19qhp5lyavt5o; 3AB9D23F7A4B3C9B=EATXFPOIBZSHZN7Z25Z4XEBA3QJI4EIYV7IH5LNZ3GGTS3LQXMSSXOHBRSMWDC6QZN7WT73IS2RERBPHP2ENXPUJXQ; TrackID=1pvYP0FyGSq3HB4MAQ_vv4xmaDQgCRYoDYc5IzT53UTeGciftAZGnZIL1L-AF0dig8TOK3wf2V3Kq1D2UCj4UGx4UpficBlwsRvlM3yWvEWk; thor=490CF693019957994840A4C6AB1A504B94B1B2E0983458AF0902E7C682048FC65F984E666FEF055E4A61A31156B9C5DF474C5B6A266F144975DD06ADEE9BE317D25164A239C5F4E20BEE6E278D3E1CD4375DB70D06E2C796615C6E705338ED914AAC9C887323E102BBDD9E0F8DB84F4903AFC82A52CCDF6113E41EDE57EDAD24BE1A8320AEB53318B0DCBBB04DD62E10; logining=1; __jda=76161171.16023462707861144776600.1602346271.1616313023.1616504845.138; __jdb=76161171.9.16023462707861144776600|138.1616504845; __jdc=76161171
cookies1 = {
    'pt_key': 'AAJgGBF1ADAyTAwIlXSurdELzj-fx4mc_ekWKh1-3esw9GtVkCLvKPdOfM_NFWU8r9HTiRyJU_I',  # cookie参数填写，填写完注意不要上传
    'pt_pin': '13693739645_p',
}

cookies2 = {}   # 如果有其它账号，还需要将cookies2填写进 下面的cookieLists

cookiesLists = [cookies1, ]  # 多账号准备


####################################
# 方案2 GitHub action 自动运行    cookies读取自secrets  
if "JD_COOKIE" in os.environ:
    """
    判断是否运行自 GitHub action, "JD_COOKIE" 该参数与 repo里的Secrets的名称保持一致
    """
    print("执行自GitHub action")
    secret = os.environ["JD_COOKIE"]
    cookiesLists = []  # 重置cookiesList
    for line in secret.split('\n'):
        pt_pin = re.findall(r'pt_pin=(.*?)&', line)[0]
        pt_key = re.findall(r'pt_key=(.*?)$', line)[0]
        cookiesLists.append({"pt_pin": pt_pin, "pt_key": pt_key})

#######################################


def valid(cookies):
    headers = {
        'Host': 'api.m.jd.com',
        'Accept': '*/*',
        'Connection': 'keep-alive',
        'User-Agent': 'jdapp;iPhone;8.5.5;13.5;Mozilla/5.0 (iPhone; CPU iPhone OS 13_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148;supportJDSHWK/1',
        'Accept-Language': 'zh-cn',
        'Accept-Encoding': 'gzip, deflate, br',
    }
    params = (
        ('functionId', 'plantBeanIndex'),
        ('body', json.dumps(
            {"monitor_source": "plant_m_plant_index", "version": "8.4.0.0"})),
        ('appid', 'ld'),
    )
    response = requests.get('https://api.m.jd.com/client.action',
                            headers=headers, params=params, cookies=cookies)
    if response.json()["code"] == "3":
        print(f"""## {cookies["pt_pin"]}: cookie过期""")
        notification.notify(
            f"""## 京东账号【{cookies["pt_pin"]}】 cookie过期""", f"""## 账号【{cookies["pt_pin"]}】 cookie过期 ，及时修改""")
        return False
    return True


def get_cookies():
    return [i for i in cookiesLists if valid(i)]


print("***"*20)
print("***"*20)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
print("\n报错请至 https://github.com/Zero-S1/JD_tools\n")

if __name__ == "__main__":
    print(">>>检查有效性")
    for i in get_cookies():
        print(i)
