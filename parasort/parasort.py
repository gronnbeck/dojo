import os
import re
import sys
import threading

file = sys.argv[1]
lock = threading.Lock()
event = threading.Event()

global Files 
Files = []
global Sorted 
Sorted= []

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
	os.popen("sort -f " + next + " > " + next + ".sorted")
	lock.acquire()
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
	os.popen("sort -fm " + pair[0] + " " + pair[1] + " > done")

def run():
	sort()
	merge()
	if len(Sorted) == 0:
		event.set()

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
print "Sorting Done"
