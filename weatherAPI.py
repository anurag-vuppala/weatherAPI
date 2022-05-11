import requests as r

url = "http://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=7d6b470e0feba322cf886d3ca22a7478"

responce = r.get(url)

d = responce.json()

print(d)










api_key = "7d6b470e0feba322cf886d3ca22a7478"

