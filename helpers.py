import argparse
from key import *
import subprocess
import requests
import json
import argparse
from argparse import RawTextHelpFormatter
import datetime
from time import sleep

#Colours
RED = '\033[91m'
ENDC = '\033[0m'
GREEN = '\033[1;32m'
WHITE = '\033[1m'
BOLD = '\033[01m'

# Copyright (c) 2019 @danlopgom 
# Edit: Modified to run with Python3, removed output to file, changed to a function
def haveibeenpwned_paste (HAVEIBEENPWNED_KEY) :
	# Get the emails
	with open('emails.dat', 'r') as f:
		emails = f.readlines()

	# Remove whitespace characters like `\n` at the end of each line
	emails = [x.strip() for x in emails]

	headers = {
		'User-Agent': 'pwncheck 2.0',
		'hibp-api-key': HAVEIBEENPWNED_KEY
		#'From': 'youremail@domain.com'  # This is another valid field
	}

	#file_pwned_urls="pwned_pastes_urls.txt"
	#file_pwned_emails="pwned_pastes_emails.txt"

	# Create the file
	#with open(file_pwned_urls, 'w'): pass
	#with open(file_pwned_emails, 'w'): pass

	# Total number of emails
	t_emails = len(emails)
	c_emails = 0
	pwned_emails = 0

	for a in emails:
		sleep(3)
		url = ('https://haveibeenpwned.com/api/v3/pasteaccount/%s') % (str(a))
		r = requests.get(url, headers=headers)
		print(40*"=")
		c_emails += 1	
		print("[+] Count: " + str(c_emails) + "/" + str(t_emails) + " (" +  str(round(100 * float(c_emails)/float(t_emails),2)) + "%)")
		
		try:
			r_json=json.loads(r.content)
		except:
			print("[+] Emails leaked for now: " + str(pwned_emails) + "/" +  str(t_emails) + " (" + str(round(100 * float(pwned_emails)/float(t_emails),2)) + ")")
			print("[+] Checking:")
			print("\t - " + BOLD + " "+ str(a) + " -> " + GREEN + "NOT leaked" + ENDC)
			continue

		count = len(r_json)
		pwned_emails += 1
		print("[+] Emails leaked for now: " + str(pwned_emails) + "/" +  str(t_emails) + " (" + str(round(100 * float(pwned_emails)/float(t_emails),2)) + ")")
		print("[+] Checking:")
		print("\t - " + BOLD + " "+ str(a) + " -> " + RED + "LEAKED" + ENDC)
		# Include the email on the external file
		#with open(file_pwned_emails, 'a') as f:
		#	f.write("%s\n" % a)
		print("[+] Leaks: " + str(count))
		print("[+] Details")

		try:
			if r_json['statusCode'] == 429:
				print(r_json)
				print("Esperamos")
				sleep(5)
				input()
		except:
			#print("We are OK")
			for c in r_json:
				print("\t- {: <30} {: <10}".format(c['Source'], c['Id']))

				#with open(file_pwned_urls, 'a') as f:
				#	if c['Source'] == "Pastebin":
				#		f.write("https://pastebin.com/%s\n" % c['Id'])
				#	elif c['Id'].startswith("http"):
				#		f.write("%s\n" % c['Id'])
	print(40*"=")

# Copyright (c) 2019 @danlopgom 
# Edit: Modified to run with Python3, removed output to file, changed to a function
def haveibeenpwned_search (HAVEIBEENPWNED_KEY) :

    # Get the emails
    with open('emails.dat', 'r') as f:
        emails = f.readlines()

    # Remove whitespace characters like `\n` at the end of each line
    emails = [x.strip() for x in emails]

    headers = {
        'User-Agent': 'pwncheck 2.0',
        'hibp-api-key': HAVEIBEENPWNED_KEY
        #'From': 'youremail@domain.com'  # This is another valid field
    }

    #file_pwned_urls="pwned_search_urls.txt"
    #file_pwned_emails="pwned_search_emails.txt"

    # Create the file
    #with open(file_pwned_urls, 'w'): pass
    #with open(file_pwned_emails, 'w'): pass

    # Total number of emails
    t_emails = len(emails)
    c_emails = 0
    pwned_emails = 0

    for a in emails:
        sleep(3)
        url = ('https://haveibeenpwned.com/api/v3/breachedaccount/%s') % (str(a))
        r = requests.get(url, headers=headers)
        print(40*"=")
        c_emails += 1	
        print("[+] Count: " + str(c_emails) + "/" + str(t_emails) + " (" +  str(round(100 * float(c_emails)/float(t_emails),2)) + "%)")

        try:
            r_json=json.loads(r.content)
        except:
            print("[+] Emails leaked for now: " + str(pwned_emails) + "/" +  str(t_emails) + " (" + str(round(100 * float(pwned_emails)/float(t_emails),2)) + ")")
            print("[+] Checking:")
            print("\t - " + BOLD + " "+ str(a) + " -> " + GREEN + "NOT leaked" + ENDC)
            continue

        count = len(r_json)
        pwned_emails += 1
        print("[+] Emails leaked for now: " + str(pwned_emails) + "/" +  str(t_emails) + " (" + str(round(100 * float(pwned_emails)/float(t_emails),2)) + ")")
        print("[+] Checking:")
        print("\t - " + BOLD + " "+ str(a) + " -> " + RED + "LEAKED" + ENDC)
        
        # Include the email on the external file
        #with open(file_pwned_emails, 'a') as f:
        #    f.write("%s\n" % a)
        print("[+] Leaked sites: " + str(count))
        print("[+] Details")
        try:
            if r_json['statusCode'] == 429:
                print(r_json)
                print("Esperamos")
                sleep(5)
                input()
        except:
            #print("We are OK")
            for c in r_json:
                print("\t- " + c['Name']) 

            #    with open(file_pwned_urls, 'a') as f:
            #        f.write(c['Name'] + "\n")
    print(40*"=")


# Copyright (c) 2020 @devanteayris
def dehashed_domain_search(DESHASHED_KEY, domain) :
    print(40*"=")
    curl_url = "curl -s 'https://api.dehashed.com/search?query=" + str(domain) + "' -u " + str(DEHASHED_EMAIL) + ":" + str(DEHASHED_KEY) + "  -H 'Accept: application/json'"
    process = subprocess.Popen(
        curl_url,
        shell=True,
        stdout=subprocess.PIPE)
    process.wait()
    data, err = process.communicate()
    data = data.decode("utf-8")
    data = data.strip()
    r_json=json.loads(str(data))
    print("[+] Checking:")
    print("[+] Leaks: " + str(len(r_json["entries"])))
    for i, leak in enumerate(r_json["entries"]) :
        print("[+] Victim: " + str(i + 1))
        if leak["email"] :
            print("\t - " + BOLD + "Email: "+ str(leak["email"]) + " -> " + RED + "LEAKED" + ENDC)
        if leak["username"] :
            print("\t - " + BOLD + "Username: "+ str(leak["username"]) + " -> " + RED + "LEAKED" + ENDC)
        if leak["password"] :
            print("\t - " + BOLD + "Password: "+ str(leak["password"]) + " -> " + RED + "LEAKED" + ENDC)
        if leak["hashed_password"] :
            print("\t - " + BOLD + "Hashed Password: "+ str(leak["hashed_password"]) + " -> " + RED + "LEAKED" + ENDC)
        if leak["name"] :
            print("\t - " + BOLD + "Name: "+ str(leak["name"]) + " -> " + RED + "LEAKED" + ENDC)
        if leak["vin"] :
            print("\t - " + BOLD + "Vin: "+ str(leak["vin"]) + " -> " + RED + "LEAKED" + ENDC)
        if leak["ip_address"] :
            print("\t - " + BOLD + "IP Address: "+ str(leak["ip_address"]) + " -> " + RED + "LEAKED" + ENDC)
        if leak["phone"] :
            print("\t - " + BOLD + "Phone: "+ str(leak["phone"]) + " -> " + RED + "LEAKED" + ENDC)
        if leak["obtained_from"] :
            print("\t - " + BOLD + "Obtained From: "+ str(leak["obtained_from"]) + " -> " + RED + "LEAKED" + ENDC)
    print(40*"=")