class person:
	def __init__(self,a,b):
		self.a=a
		self.b=b
		print("Name=",self.a)
		print("Age=",self.b)
name=input("Enter the name")
age=eval(input("Enter the age"))
p1=person(name,age)