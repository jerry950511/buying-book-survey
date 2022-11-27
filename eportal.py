import requests
from bs4 import BeautifulSoup
import json
def check_eportal(account,password):

    response = requests.get("https://wane.nutc.edu.tw/dm_device/device1.php?eportal_id="+account+"&eportal_passwd="+password+"&out=mem_check")

    text = response.text
    pretext = ')]}\''
    text = text.replace(pretext,'')
    # 把字串讀取成json
    soup = json.loads(text)
    if soup["res_echo"] == "pass":
        return True
    else:
        return False
def get_info(account,password):

    response = requests.get("https://wane.nutc.edu.tw/dm_device/device1.php?eportal_id="+account+"&eportal_passwd="+password+"&out=mem_check")

    text = response.text
    pretext = ')]}\''
    text = text.replace(pretext,'')
    # 把字串讀取成json
    soup = json.loads(text)
    if soup["res_echo"] == "pass":
        infodict = {"學號":soup["st_id"],"姓名":soup["st_name"],"手機":soup["phone"]}
        print(infodict)
        return infodict
    else:
        return False
        