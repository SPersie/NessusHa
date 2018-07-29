from bs4 import *
import re

def foo():
	host = {}
	output = []
	lines = []
	rawhtml = open("C:\\Users\\rsakthi\\Desktop\\Meritus\\Windows\\test.html", encoding="utf-8").read()
	bs = BeautifulSoup(rawhtml,"html.parser")
	# for i in bs.find_all('h2'):
	# 	j = i.get_text()
	# 	if j in host.keys():
	# 		host[j] += 1
	# 	else:
	# 		host[j]=1
	# output = [a.get_text().replace('\n','') for a in bs.find_all('div',style="box-sizing: border-box; width: 100%; background: #eee; font-family: monospace; padding: 20px; margin: 5px 0 40px 0;")]
	# print(output)
	# check = [a.get_text().replace('\n','') for a in bs.find_all('div',style="box-sizing: border-box; width: 100%; margin: 0 0 10px 0; padding: 5px 10px; background: #d43f3a; font-weight: bold; font-size: 14px; line-height: 20px; color: #fff;")]
	# print(check)
	# print(host)
	print(bs.get_text())
	
foo()

	