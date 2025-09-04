'''
a=5         #integer
b=5.5       #float
c="divya"    #string
print(type(a))
print(type(b))
print(type(c))
print(id(a))
print(id(b))
print(id(c))

#reverse a number using while loop
num=123456
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)    

num=12345654321
num1=num
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev) 
if (num1==rev):
    print("given number is palindrome")
else:
    print("given number is not a palindrome")

num=123456
num1=num
if num%10!=0:
    rev=0
    while num>0:
        ld=num%10
        rev=rev*10+ld
        num=num//10
    print(rev)
    if num1==rev:
        print("palindrome")
    else:
        print("not palindrome")
else:
    print("given number which are not divisible by 10 because we cannot check for palindrome")

num=int(input("enter the number:"))
sum=0
temp=num
n=len(str(num))
while(temp>0):
    digit=temp%10
    sum+=digit**n
    temp=temp//10
print(sum)
if sum==num:
    print("armstrong")
else:
    print("not armstrong")       

num=int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print("not prime")
            break
        else:
            print("prime")
            break
else:
    print("invalid syntax")    
 
num=123456
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)         

num=int(input("enter the number:"))
sum=0
temp=num
n=len(str(num))
while(temp>0):
    digit=temp%10
    sum+=digit**n
    temp=temp//10
print(sum)
if sum==num:
    print("armstrong")
else:
    print("not armstrong") 

num=123454321
num1=num
rev=0
while num>0:
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev)
if num1==rev:
    print("palindrome")
else:
    print("not palindrome")  

a="divyachitti" 

print(len(a))    

num=int(input("enter the number:"))
sum=0
for x in range(1,num):
    if num%x==0:
        sum+=x
    print(x)
if sum==num:
    print("perfect number")
else:
    print("not perfect number") 

def perfectnumber(num):
    sum=0
    for x in range(1,num):
        if num%x==0:
            sum+=x
    if sum==num:
        return True
    else:
        return False
op=[x for x in range(1,50) if perfectnumber(x)]
print(op) 

num=int(input("enter the number:"))
isperfect=False
for x in range(1,num):
    if x**2==num:
        isperfect=True
        break
if isperfect:
    print("perfect sqare")
else:
    print(" not perfect sqare")

#creat a list of perfectsqares using comprehension
def perfectsqare(num):
    isperfect=False
    for x in range(1,num):
        if x**2==num:
            isperfect=True
            break
    if(isperfect):
        return True
    else:
        return False
op=[x for x in range(1,101) if perfectsqare(x)] 
print("list of perfect square numbers are:", op)  

#create list of perfectnumbers using comprehensions
def perfectnumber(num):
    sum=0
    for x in range(1,num):
        if num%x==0:
            sum+=x
    if sum==num:
        return True
    else:
        return False
op=[x for x in range(1,101) if perfectnumber(x)]
print("list of perfect numbers are:", op)            

#create list of neon numbers using comprehensions
def neonnumber(num):
    square=num**2
    sum=0
    while(square>0):
        ld=square%10
        sum+=ld
        square=square//10
    if sum==num:
        return True
    else:
        return False     
op=[x for x in range(1,101) if neonnumber(x)]
print("list of neon numbers are:", op) 

#create list of sunny numbers using comprehensions
def sunnynumber(num):
    issunny=False
    for x in range(1,num):
        if (x**2==num+1):
            issunny=True
            break
    if issunny:
        return True
    else:
        return False
op=[x for x in range(1,101) if sunnynumber(x)]
print("list of sunny numbers are:", op)  

#list of prime numbers using comprehensions
def primenumber(num):
    isprime=True
    if num<=1:
        print("please give number greater than 1")
    else:
        for x in range(2,num):
            if num%x==0:
                isprime=False
                break
        if isprime:
            return True
        else:
            return False
op=[x for x in range(2,101) if primenumber(x)]
print("list of prime numbers are:", op) 

#create list of reversed strings using comprehensions
str1=["divya","chitti","cryso","asha"]
reversed_strings=[word[::-1] for word in str1]
print(reversed_strings)
'''

#Method Overriding
class vehicle:
    def speed(self):
        print("vehicle speed is normal")
class car(vehicle):
    def speed(self):
        print("car speed is 120kmph")
class cycle(vehicle):
    def speed(self):
        print("cycle speed is 20kmph")  
car=car()
cycle=cycle()
car.speed()
cycle.speed()              


class order:
    def __init__(self,customer,order_id):
        self.customer=customer
        self.order_id=order_id
    def deliver(self):
        print(f"{self.customer} will get this order number {self.order_id} with standerd delivery") 
class expressorder(order):
    def __init__(self,customer,order_id):
        super().__init__(customer,order_id)
    def deliver(self):
        print(f"{self.customer} will get this order number {self.order_id} with express delivery")
obj1=order("chitti","chitti234")
obj1.deliver()
obj2=order("divya","divya654")
obj2.deliver()
obj3=expressorder("cryso","cryso876")
obj3.deliver()
print(obj1.__dict__)
print(obj2.__dict__)
print(obj3.__dict__)
print(expressorder.__mro__)

#encapsulation
#private
class sample:
    def __init__(self):
        self._name="chitti"
obj=sample()
print(obj._name)  

class parent:
    def __init__(self):
        self._user="divya"
class child(parent):
    def __init__(self):
        super().__init__()
        print(self._user)
obj1=child()
print(obj1._user)        

class sample:
    def __init__(self):
        self._name="chitti"
    def getdetails(self):
        print(self._name)
obj=sample()
print(obj.getdetails())        

class demo:
    def __init__(self):
        self.name="cryso"
obj=demo()
print(obj.__dict__)  
obj.name="chitti"
obj._name="divya"
obj.__name="cryso"
print(obj.__dict__)  

class demo:
    def __init__(self):
        self.__name="divya"
    def setdetails(self):
        self.__name="chitti"
obj=demo()
print(obj.__dict__)
obj.setdetails()
print(obj.__dict__)            