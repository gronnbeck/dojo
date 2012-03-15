#!/usr/bin/python

import os
import re
import sys
import threading
import subprocess
import random

file = sys.argv[1]
processes = 2

SPLIT_PREFIX = file + str(random.randint(0,2**16))

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

def split(filename):
	subprocess.call(["split -l " + str(linecount(filename)/processes) + " " + filename + " " + SPLIT_PREFIX], shell=True)


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

split(file)

for i in os.popen("ls"):
	match = re.search(SPLIT_PREFIX + "[\w]+", i)
	if not match:
		continue
	Files.append(match.group(0))

threads = []

for i in range(processes):
	threads.append(threading.Thread(target=run))

for thread in threads:
	thread.start()
 
event.wait()
