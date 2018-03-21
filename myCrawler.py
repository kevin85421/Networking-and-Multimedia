
import urllib.request as urllib
import http
import sys
from urllib.error import URLError
import queue
from threading import Thread
import time

# read lines

with open('all.txt') as f:
    lines = f.readlines()

# global variable
remain = len(lines)
que = queue.Queue()
#fo = open("result.txt", "w")


class Job:
	def __init__(self, webaddress, line):
		self.url = webaddress + '/' + line
	def do(self):
		global remain
		global fo
		remain = remain -1 
		try:
			page = urllib.urlopen(self.url)
			if page.getcode() >= 200 and page.getcode() < 300:
				print(self.url)
		except http.client.HTTPException as e:
			pass
		except urllib.HTTPError as e:
			pass
		except URLError as e:
			pass	
	



def doJob(*args):  
     queue = args[0]  
     while queue.qsize() > 0:  
          job = queue.get()  
          job.do()  


if __name__=="__main__":  
    webaddress = input("Input the Website Address : ") 
    threads = []
    for line in lines :
    	que.put(Job(webaddress,line))

    for num in range(0,100):
   		_thread = Thread(target=doJob, args=(que,))
   		threads.append(_thread)
   		_thread.start()
    #getDirectory(webaddress)
    while remain != 0:
    	time.sleep(1) #wait 
    	print(str(len(lines)-remain)+'/'+str(len(lines)))
    for _thread in threads:
    	_thread.join()
    print("Well done")

    

	