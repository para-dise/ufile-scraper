import random
import string
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from threading import Thread

gay = []

def ran(size=5, chars=string.ascii_letters + string.digits):
    e = ''.join(random.choice(chars) for x in range(size))
    if e not in gay:
      return e
    gay.append(e)

def scrapefile():
  time.sleep(.1)
  link = ran()
  fileurl = 'https://217.182.136.95/' + link
  asd = requests.get(fileurl, verify=False)
  if asd.status_code == 200 and "Sorry it's gone..." not in asd.text:
    print('\33[32mValid link: '+ fileurl + "\33[0m")
    f = open("working.txt", "a")
    f.write(fileurl + "\n")
    f.close()
  else:
    pass


for i in range(1,10000000):
  t = Thread(target=scrapefile)
  t.start()
