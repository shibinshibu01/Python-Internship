'''
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def introduce(self):
		#print("My name is " , self.name , "and my age is " , self.age)
		print(f'My name is {self.name} and my age is {self.age}\n')		

class Car:
	def __init__(self, brand, color, year):
		self.brand = brand
		self.color = color
		self.year = year
	def introduce(self):
		print(f'Car:{self.brand}\nColor:{self.color}\nYear:{self.year}\n\n')

p1 = Person("Shibin",22)
p2 = Person("Gopal",21)

c1 = Car("BMW","Red",2020)
c2 = Car("Benz","Blue",2023)
c3 = Car("Audi","White",2022)

p1.introduce()
p2.introduce()

c1.introduce()
c2.introduce()
c3.introduce()
'''

file = open("file.txt")
print(file.read())
file.close()
x='''After dark on Saturday night one could stand on the first tee of
the golf-course and see the country-club windows as a yellow expanse
over a very black and wavy ocean. The waves of this ocean, so to speak,
were the heads of many curious caddies, a few of the more ingenious
chauffeurs.'''
file = open("file.txt",'w')
file.write(x)
file.close()
file = open("file.txt",'r')
print(file.read())