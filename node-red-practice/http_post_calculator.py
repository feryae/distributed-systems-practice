import requests

url = "http://IPADDRESS:1880/post-calculator"

angka1 = 0
angka2 = 0
equ = ""
while True:
    print "Input angka 1"
    angka1 = int(input())
    print "Input angka 2"
    angka2 = int(input())
    print "Input equation"
    equ = raw_input()
    datax = {"no1":angka1, "no2":angka2, "eq":equ}
    
    r = requests.post(url, json=datax)

    print r

    print r.text