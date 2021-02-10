class theory:
	def __init__(self,a,b,c):
		self.tm1=a
		self.tm2=b
		self.tm3=c
class practical:
	def __init__(self,a,b,c):
		self.pm1=a
		self.pm2=b
		self.pm3=c
class marks(theory,practical):
	def __init__(self,a,b,c,d,e,f):
		super().__init__(a,b,c)
		practical.__init__(self,d,e,f)
	def tot(self):
		total=0
		total=self.tm1+self.tm2+self.tm3+self.pm1+self.pm2+self.pm3
		print("The total=",total)
s1=marks(34,55,66,77,88,22)
s1.tot()