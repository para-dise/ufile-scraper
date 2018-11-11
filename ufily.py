import random
import string
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def ran(size=5, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

for i in range(1,10000000):
    time.sleep(.1)
    link = ran()
    
    inviteurl = 'https://217.182.136.95/'+link
    asd = requests.get(inviteurl, verify=False)
    print(asd)
    print('attempted code: '+inviteurl)
