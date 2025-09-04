'''sets={1,2,3,4,5}
print(type(sets))
print(sets)

sets.add("hi")
print(sets)

sets.remove(3)
print(sets)

set1=frozenset([1,3,5,7,8,8])
print(type(set1))
print(set1) 

print(type(3.14))
x=5+3*2
print(x)
x="python"
print(f"language:,{x}")

print(type(True))

x=5
y=2
print((x//y)+(x%y))

a=10
b=10.0
print(a==b)

x=153 21 79 232
y=sorted(str1)
print(x)
'''

#abstraction
from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def travelvehicle(self):
        pass
class car(vehicle):
    def travelvehicle(self):
        print("travel by using car")
class bike(vehicle):
    def travelvehicle(self):
        print("travel by using bike")  
class train(vehicle):
    def travelvehicle(self):
        print("travel by using train") 
c=car()
b=bike()
t=train()
c.travelvehicle()
b.travelvehicle()
t.travelvehicle()

