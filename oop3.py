class partyanimal:
	name=""
	x=0
	def __init__(self,a):
		self.name=a
		print(self.name,"Constructed")
	def party(self):
		partyanimal.x=partyanimal.x+1
		print(partyanimal.x,"This is the party count")
	def __del__(self):
		partyanimal.x-=1
s=partyanimal("raj")
s.party()
s.party()
t=partyanimal("carrom")
t.party()
del(t)
del(s)

