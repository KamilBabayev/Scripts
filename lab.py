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

inst1 = Demo("Admin Mark")
print(inst1.name)
print(inst1.get_name())
inst1.name = "David David"
print(inst1.name)









###################################################################
#   Classes, Inheritance
print (20* '--')
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
