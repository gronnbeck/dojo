#!/usr/bin/python

import os
import re
import sys
import threading
import subprocess

file = sys.argv[1]
lock = threading.Lock()
event = threading.Event()

global Files 
Files = []
global Sorted 
Sorted= []

def remove(file):
	subprocess.call(["rm " + file], shell=True)

def linecount(filename):
	return int(re.search("[0-9]+", os.popen("wc -l " + filename).readline()).group(0))

def next2sort():
	lock.acquire()
	r = False
	if len(Files) != 0:
		r = Files.pop()
	lock.release()
	return r	

def sort():
	next = next2sort()
	if not next:
		return
	subprocess.call(["sort -f " + next + " > " + next + ".sorted"], shell=True)
	lock.acquire()
	remove(next)
	Sorted.append(next + ".sorted")
	lock.release()

def pair2merge():
	lock.acquire()
	pair = False
	if len(Sorted) == 2:
		pair = (Sorted.pop(), Sorted.pop())
	lock.release()
	return pair

def merge():
	pair = pair2merge()
	if not pair:
		return
	subprocess.call(["sort -fm " + pair[0] + " " + pair[1] + " > " + file + ".sorted"], shell=True)
	lock.acquire()
	remove(pair[0])
	remove(pair[1])
	lock.release()

def run():
	sort()
	merge()
	lock.acquire()
	if len(Sorted) == 0:
		event.set()
	lock.release()

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
