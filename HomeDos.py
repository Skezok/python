#!/usr/bin/python3

import requests
import time

def main(googleHome):

	while True:
		
		homeURI = "http://" + googleHome + ":8008/setup/reboot"
		headers = {'content-type':'application/json'}
		data = '{"params":"now"}'
		request = requests.post(homeURI, headers=headers, data=data)
		time.sleep(60)

if __name__ == "__main__":
	googleHome = input("Entrez l'IP de votre Google Home : ")
	main(googleHome)