class partyanimal:
	name=""
	x=0
	def __init__(self,n):
		self.name=n
		print(self.name,"constructed")
	def party(self):
		self.x+=1
		print("count of party is ",self.x)
class football(partyanimal):
	point=0
	def touch(self):
		self.point+=7
		self.party()
		print(self.name,self.point)
s=partyanimal("Yuvraj")
s.party()
s.party()
k=football("Raj")
k.touch()