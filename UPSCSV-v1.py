#!usr/bin/env/python2

"""""
UPSCSV-v1 021220
Fix program to be used for IoT ups monitoring on atm v.1
data logger to csv every 15 minutes and getting taken by IoT programs.
fix the clock!
CRN
"""""
#_init_
import subprocess
import time
import CSV
subprocess.run(['upsdrvctl','start'])
dataupslist=[]
#loop
Try:
while True:
	#if time.strftime:
	
		dataups = subprocess.check_output(['upsc'],['ups'])
		dataupsstr =dataups.decode('UTF-8').split('\n')
		dataupslistraw = list(i.split(': ') for i in (dummydecodedtolist))
		for i in dataupslistraw:
			if len(i) == 2:
				dataupslist.append(i)
			else:
				continue
	
		dataupsdict=dict(dataupslist)
		with open
		dataupslist=[]
		time.sleep(60)
