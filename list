#!/usr/bin/python3
import subprocess

data = subprocess.check_output(["upsc", "upsilon"])
decoded_data = data.decode("utf-8").split('\n') #keluaran list
decoded_data = [i.split() for i in decoded_data] #keluaran list lagi dalemnya

for i in range(len(decoded_data)):
	print(i, decoded_data[i])
