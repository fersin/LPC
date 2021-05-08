import requests

#api #1
ip=input("ingrese la ip que desea en formato ipv4")
r=requests.get('http://api.ipapi.com/api/'+ip+'?access_key=b7b979141c657937ac4b05df225c0ca9')

print(r.text)

#api #2
a=input("ingrese la ciudad que quiera ")

api_address = 'http://api.openweathermap.org/data/2.5/weather?appid=7cb793fd1e6bc19d787d866b4374a320&q='
url = api_address + a
json_data = requests.get(url).json()
format_add = json_data['weather'][0]["description"]
print(format_add)
