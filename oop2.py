class person:
	def __init__(self,a,b):
		self.name=a
		self.age=b
		print("Name=",self.name)
		print("Age=",self.age)
	def add(self,a,b):
		self.a=a
		self.b=b
		c=0
		c=self.a+self.b
		print(c)
name=input("Enter the name")
age=eval(input("Enter the age"))
p1=person(name,age)
p1.add(34,35)
