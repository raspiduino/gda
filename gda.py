'''
gda.py - Python script for Google Drive download (large files) with the help of aria2
Copyright @raspiduino 2020
Date created 25/12/2020 - Christmas
'''

import requests
import os
import sys

helpstring = '''
gda.py - Python script for Google Drive download (large files) with the help of aria2
Copyright @raspiduino 2020
Date created 25/12/2020 - Christmas

Usage:
gda.py file/help fileid
fileid        : Paste in the file/folder id, for example if the link is https://drive.google.com/file/d/abc
                please type in abc

Note: + By default this python script will download at max speed using aria2 '-x16 -s16 -j5' option. You
can remove it if you don't want to.
      + You can add more command line to aria2 if you want
'''

if sys.argv != [""]:
	# Download a single file
	if sys.argv[1] != "":
			# Get the cookies
			session = requests.Session()
			session.get("https://drive.google.com/uc?export=download&id=" + sys.argv[1])
			cookiename = list(session.cookies.get_dict().keys())[0]
			cookieval = list(session.cookies.get_dict().values())

			# Execute the aria2c command
			errorcode = -1
			while errorcode != 0:
				# Run until there is no error
				# Restart if error occur
				errorcode = os.system('aria2c -x16 -s16 -j5 --header="Cookie: ' + cookiename + '=' + cookieval[0] + '" --header="Cookie: NID=' + cookieval[1].replace("=", "%22") + '" "https://drive.google.com/uc?export=download&confirm=' + cookieval[0] + '&id=' + sys.argv[1] + '"')

	elif sys.argv[1] == "help":
		print(helpstring)

	else:
		print("Please enter a file id!")
		print(helpstring)
			