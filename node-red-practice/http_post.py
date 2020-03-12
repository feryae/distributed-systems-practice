import requests

url = "http://IPADDRESS:1880/int-json"
datax = {"var1":var, "var2":var, "eq":var}
    
r = requests.post(url, json=datax)

print r
print r.text