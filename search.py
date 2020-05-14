from requests import *
import re
import sys

url = ""

TR = re.compile('<TR>(.*?)</TR>',re.DOTALL)
TD = re.compile('<TD>(.*?)</TD>')
domains = []

def Check_Syntax():

	global url
	
	if(len(sys.argv) < 2 ):
	
		exit("[!] python3 search.py {%.domain}")
	
	url = sys.argv[1]

def Search():
	
	global domains

	res = get("https://crt.sh/?q={}".format(url))
	for i in TR.findall(res.text):
	
		if(i.find('<TD style="text-align:center">') != -1):
	
			for j in TD.findall(i)[0].split("<BR>"):
	
				domains.append(j)

	domains = list(set(domains))

def Result_Print():

	global domains

	print("[*] Found {} Sub-domains\n".format(len(domains)))
	for domain in domains:

		print("[+] {}".format(domain))


def main():
	
	Check_Syntax()
	Search()
	Result_Print()


if __name__ == '__main__':

	main()
