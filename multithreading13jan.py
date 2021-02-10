from time import *
from threading import *
class hello(Thread):
	def run(self):
		for i in range(8):
				print("hello")
				sleep(1)
				
class hi(Thread):
	def run(self):
		for i in range(8):
			print("hi")
			sleep(1)
			
t1=hello()
t2=hi()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("bye")


