#!/usr/bin/env python3
# Setters and Getters, in python obj attribues are open from outside. you can
# write setters and getters to close direct access. It would be correct if we do it 
# vi properties.

class Demo:
	def __init__(self, input_name):
		self.hidden_name = input_name
	def get_name(self):
		print('inside the getter')
		return self.hidden_name
	def set_name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name
	name = property(get_name, set_name)		# here getter & and setter becomes as
											# name property of object.
# when we write  obj.name  - obj.get_name is called, when we do obj.name = "Ka New"
# obj.set_name('Ka New') is called 

inst1 = Demo("Old User")
print(inst1.get_name())
inst1.set_name("New User")
print(inst1.get_name())

# Other method is using decorators  @property -for getter, @name.setter -for setter
print('setter getter with decorator method')
class NewClass:
	def __init__(self, input_name):
		self.hidden_name = input_name
	@property
	def name(self):
		print('inside the getter decorator')
		return self.hidden_name
	@name.setter
	def name(self, input_name):
		print('inside the setter decorator')
		self.hidden_name = input_name

print(' decorator method ' )
inst2 = NewClass("DemoNAme")
print(inst2.name)
inst2.name = "Newest User"
print(inst2.name)


print('----------------------')
class Circle():
	def __init__(self,radius):
		self.radius=radius
	@property
	def diameter(self):
		return 2 * self.radius

c = Circle(5)
print(c.radius)
print(c.diameter)

###################################################################
#   Classes, Inheritance
print(20* '--')
print('Classes part\n')

class Father:
	def __init__(self, sname):
		self.sname = sname

class Son(Father):
	def __init__(self,sname,name):
		super().__init__(sname)
		self.name = name

user1 = Son("Kamil", "Babayev")
print(user1.name, user1.sname)
