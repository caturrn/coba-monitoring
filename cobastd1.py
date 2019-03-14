#!usr/bin/env/python3

##init 1 time
import datetime
import subprocess
import time

subprocess.run(['upsdrvctl','start'])

class Queue:

  #Constructor creates a list
  def __init__(self):
      self.queue = list()

  #Adding elements to queue
  def enqueue(self,data):
      self.queue.insert(0,data)

  #Removing the last element from the queue
  def dequeue(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("Queue Empty!")

  #Getting the size of the queue
  def size(self):
      return len(self.queue)

  #printing the elements of the queue
  def printQueue(self):
      return self.queue

#buat class untuk connection, perlukah?

###########################
#loop program

voltage = Queue()
frequency = Queue()
dataupslist=[]

While True:
	dataups = subprocess.check_output(['upsc'],['ups'])
	dataupsstr =dataups.decode('UTF-8').split('\n')
	dataupslistraw = list(i.split(': ') for i in (dummydecodedtolist))

	for i in dataupslistraw:
		if len(i) == 2:
			dataupslist.append(i)
		else:
			continue
	dataupsdict=dict(dummylist)
	voltage.enqueue(dictdummy['Voltage'])
	if len(voltage) == 4:
		print(voltage)
		voltage.dequeue()
	time.sleep(60)
	



