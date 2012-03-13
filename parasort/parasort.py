#!/usr/bin/python

import os
import re
import sys
import threading
import subprocess

file = sys.argv[1]
event = threading.Event()

global Files 
Files = []
fileslock = threading.Lock()

global Sorted 
Sorted= []
sortedlock = threading.Lock()

def remove(file):
	subprocess.call(["rm " + file], shell=True)

def linecount(filename):
	return int(re.search("[0-9]+", os.popen("wc -l " + filename).readline()).group(0))

def next2sort():
	fileslock.acquire()
	r = False
	if len(Files) != 0:
		r = Files.pop()
	fileslock.release()
	return r	

def sort():
	next = next2sort()
	if not next:
		return
	subprocess.call(["sort -f " + next + " > " + next + ".sorted"], shell=True)
	sortedlock.acquire()
	remove(next)
	Sorted.append(next + ".sorted")
	sortedlock.release()

def pair2merge():
	sortedlock.acquire()
	pair = False
	if len(Sorted) == 2:
		pair = (Sorted.pop(), Sorted.pop())
	sortedlock.release()
	return pair

def merge():
	pair = pair2merge()
	if not pair:
		return
	subprocess.call(["sort -fm " + pair[0] + " " + pair[1] + " > " + file + ".sorted"], shell=True)
	remove(pair[0])
	remove(pair[1])

def run():
	sort()
	merge()
	sortedlock.acquire()
	if len(Sorted) == 0:
		event.set()
	sortedlock.release()

os.popen("split -l " + str(linecount(file)/2) + " " + file + " xx")
Files = []
for i in os.popen("ls"):
	match = re.search("xx[\w]+", i)
	if not match:
		continue
	Files.append(match.group(0))

threads = []

def test():
	print "test"
	event.set()

for i in range(2):
	threads.append(threading.Thread(target=run))

for thread in threads:
	thread.start()
 
event.wait()
