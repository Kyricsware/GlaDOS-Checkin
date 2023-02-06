import requests,json

# 填入glados账号对应cookie
cookie = ''



url= "https://glados.rocks/api/user/checkin"

referer = 'https://glados.rocks/console/checkin'

proxies = {"http":None,"https":None}

data = {"token":"glados.network"}

checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer } , proxies=proxies , data=data)
print(checkin.text)





