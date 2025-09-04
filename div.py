#problems on lists
#create a list of 5 integers
'''list=[1,2,3,4,5]
print(list)
#access 3rd element of a list
list=[20,30,40,50,60]
print(list[2])
#change value at index 2
list=[10,20,30,40,50]
list[2]=60
print(list)
list.append(70)  # append an elemnet to the list
print(list)
list.insert(1,25)    #insert an element at index 1
print(list)
list.remove(25)     # remove an element by value
print(list)
list=[10,20,30,40,50]
list.pop(0)       #remove an elemnet by index
print(list)
print(len(list))   #find length of the list
#check if an element exists in a list
list=[10,20,30,40,50]
if 30 in list:
    print(" 30 exists in list")
else:
    print(" 30 doesnt exists")    
#loop through a list and print each item
list=[10,20,30,40,50]  
for item in list:
    print(item)
#sort a list in ascending order
list=[90,80,30,70,50]
list.sort()
print(list)
list.sort(reverse=True)  # sort a list in descending order
print(list)
#reverse a list using reverse()
list=[10,20,30,40,50]
list.reverse()
print(list)
#reverse a list using slicing
list=[90,80,30,70,50]
reverse=list[::-1]
print(reverse)
#copy a list using slicing 
list=[90,80,30,70,50]
list1=list[:]
print(list1)
#copy a list using copy() method
list=[1,2,3,4,5,6]
list.copy()
print(list)
#clear all elements in list
list=[90,80,30,70,50]
list.clear()
print(list)
#count accurences of a number
list=[1,4,6,3,1,3,6,8,1,7,6,1]
print(list.count(1))
#find index of a number
list=[90,80,30,70,50]
x=list.index(30)
print(x)
#concatenate 2 lists
list=[90,80,30,70,50]
list1=[1,4,6,3,1,3,6,8,1,7,6,1]
list.extend(list1)
print(list)
#concatenation
list=[90,80,30,70,50]
list1=[1,4,6,3,1,3,6,8,1,7,6,1]
combine=list+list1
print(combine)
#repeate a list 3 times
list=[90,80,30,70,50]
repeat=list*3
print(repeat)
#print every second element
list=[90,80,30,70,50,60]
print(list[1::2])
#print every second element
list=[90,80,30,70,50,60]
for i in range(1,len(list),2):
    print(list[i])
#print elements from index 2 to 5
list=[90,80,30,70,50,60,10]  
print(list[2:6])
#check if all elements are positive
x=[90,80,30,70,50,60,10]
if (num>0 for num in list):
    print("positive")
else:
    print("negative")
#convert list to a string with commas
x=["apple","banana","mango"]
y=','.join(x)   
print(y)  
#find max element
x=[90,80,30,70,50,60,10]
y=max(x)
print(y)
#find min element
x=[90,80,30,70,50,60,10]
y=min(x)
print(y)
#summ of all numbers in a list
x=[90,80,30,70,50,60,10]
y=sum(x)
print(y)
#sqare every number in a list
list=[90,80,30,70,50,60,10]
y=[x**2 for x in list] 
print(y)
#e=filter even numbers from list
list=[90,85,30,75,50,65,10]
y=[ x for x in list if x%2==0]
print(y) 
#filter odd numbers from list
list=[90,85,30,75,50,65,10]
y=[x for x in list if x%2!=0]
print(y)
#find duplicates in list
list=[90,85,30,75,50,65,10,30,90,75]
x=set()
y=set()
for item in list: 
    if item in y:
        x.add(item)
    else:
        y.add(item) 
print(x)         
#remove duplicates from list
list1=[1,2,3,2,4,5,3,6,3]
unique_list=[]
seen=set()
for item in list1:
    if item not in seen:
        unique_list.append(item)
        seen.add(item)
print(unique_list) 
#get unique elements using set()
list1=[1,2,3,2,4,5,3,6,3]
unique_list=set(list1)
print(unique_list)
#
list1=[1,2,3,2,4,5,3,6,3]
unique_elements=set(list1)
print(unique_elements)
#check if a list is empty
list2=[]
if len(list2)==0:
    print("list is empty")
else:
    print("list is not empty")  
#initialize a list of n zeros
n=5
list=[0]*n      
print(list)
#swap 2 elements in a list
list1=[10,20,30,40]
list1[1], list1[3]=list1[3],list1[1]
print(list1)
#get last element of a list
list1=[10,20,30,40]
print(list1[3])
#convert a string to a list of chars
str1="chitti"

#problems on loop
#print numbers 1 to 10 using loop
for i in range(1,11):
    print(i)
#print even numbers from 1 to 20  
for i in range(1,21):
  if i%2==0:
    print(i,end=",")   
#Print odd numbers from 1 to 20.
for i in range(1,21):
  if i%2!=0:
    print(i, end=",")
#Calculate the sum of numbers from 1 to 100.
total=sum(range(1,101))
print(total)
#Print multiplication table of 5.
def mul(num):
    for x in range(1,11):
      print(f"{num} x {x} = {num*x}")
mul(5)      
#Print all numbers divisible by 3 up to 50.
for i in range(1,51):
    if i%3==0:
        print(i, end=" ")
#Calculate the factorial of a number using a loop
num=int(input("enter the number:"))
factorial=1
if num<0:
    print("give positive number")
else:
    for i in range(1, num+1):
     factorial*=i 
print(f"factorial of a {num} is {factorial}.")        
#Reverse the digits of a number using a loop.
num=int(input("enter the number:"))
reversed_num=0
original_num=num
temp=abs(num)
while temp!=0:
    digit=temp%10
    reversed_num=reversed_num*10+digit
    temp=temp//10
print(reversed_num)
#Print squares of numbers from 1 to 10.
for i in range(1,11):
    print(i**2)
#Count the number of digits in an integer.
def count_digits(n):
  return len(str(n))
value=int(input("enter the value:"))
print(count_digits(value))  
#Find the sum of digits of a number.
sum=0
value=str(input("enter the value:"))    
for i in value:
    sum+=i
    print(sum)
#Print powers of 2 up to 2^10.
for i in range(1,11):
    print(f"2^{i}={2**i}")
#Check if a number is prime using a loop.
num=int(input("enter the number:"))
if num>0:
    for i in range(2,num):
        if num%i==0:
            print("not a prime number")
            break
        else:
            print("prime number")
            break
else:
    print("invalid number")                    
#Print first 10 natural numbers using while loop.
i=1
while i<=10:
    print(i)
    i+=1
#Count down from 10 to 1 using a loop.
for i in  range(10,0,-1):
    print(i)
#Find product of all numbers from 1 to 10.
product=1
for i in range(1,11):
    product*=i
    print(product)
#Print numbers from 1 to 100 in steps of 5.
for i in range(1,101,5):
    print(i)
#Find numbers between 1 to 50 divisible by both 3 and 5.
for i in range(1,51):
    if i%3==0 and i%5==0:
        print(f"divisible by both 3 and 5 is {i}")
#Print all prime numbers between 1 to 50.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
   return True
for num in range(1, 51):
    if is_prime(num):
        print(num)
#Display the reverse of an integer.
x=int(input("enter the value:"))
reverse=str(x)[::-1]
print(reverse)
#Find the smallest digit in a number.
x=str(input("enter the value:"))
smallest=min(x)
print(smallest)
#Find the largest digit in a number.
x=int(input("enter the value:"))
y=str(x)
largest=max(y)
print(largest)
#Print pattern: 1 2 3, 4 5 6, 7 8 9
for x in range(1,10):
    str=0
    for y in range(x+1):
        str=str*10+y
    print(str) 
#Print pattern of stars in triangle format.
for x in range(1,6):
    line=""
    for y in range(x):
        line+="*"
print(line)
#Print sum of odd digits in a number.
num=(input("enter the number:"))
sum=0
for x in num:
    if int(x)%2==0:
       sum+=int(x)
print(sum)
#Print table of a given number.
def mul(n):
    for x in range(1,11):
        print(f"{n} x {x} = {n*x}")
mul(12)        
#Count how many times a digit occurs in a number.

#Sum of squares of digits of a number.
x=input("enter the number:")
sum=0
for digit in x:
    op=(int(digit)**2) 
    print(op)
    sum+=op
print("sum of the sqares of digits is:", sum)
#Sum of cubes of digits of a number.
y=input("enter the number:")
sum=0
for digit in y:
    op=(int(digit)**3)
    print(op)
    sum+=op
print("sum of cubes of digits is:",sum)    
#Print sum of even digits in a number.
z=input("enter the number:")
sum=0
for digit in z:
   if int(digit)%2==0:
      print(digit)
      sum+=int(digit)
print("sum of even digits is:",sum)   
#Count multiples of 3 between 1 and 100.
count=0
for i in range(1,101):
    if i%3==0:
        print(i, end=" ")
#Print 10, 20, 30... up to 100.
for i in range(0,100,10):
   print(i, end=" ")
#Print reverse of a number using while loop.
num=123456
rev=0
while(num>0):
    ld=num%10
    rev=rev*10+ld
    num=num//10
print(rev) 
#Find if number is Armstrong number (3-digit only)
num=int(input("enter the number:"))
n=len(str(num))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum+=digit**n
    temp//=10
if num==sum:
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")    
#Print Fibonacci series up to n terms.
num=int(input("enter the number:"))
a=0
b=1
count=0
while (count<num):
    print(a," ",end="")
    temp=a+b 
    a=b 
    b=temp
    count+=1      
#Print GCD of two numbers using loop.

#Print LCM of two numbers using loop.
#Display all even digits in a number.
num=input("enter tha value:")
for digit in num:
    if int(digit)%2==0:
        print(digit)
#Display all odd digits in a number.
num=input("enter the number:")
for digit in num:
    if int(digit)%2!=0:
       print(digit)
#Print the ASCII values from 65 to 90.
for i in range(65,90):
    print(f"{i} - {chr(i)}")

#problems on tuple
#Create a tuple with 5 elements and print it.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(days)
#Access the third element of a tuple.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(days[2])
#Slice a tuple to get the first 3 elements.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(days[:3])
#Check if an item exists in a tuple.
days=("sun","mon","tue","wed","thurs","fri","sat")
item="wed"
if item in days:
    print(f"{item} exists in tuple") 
else:
    print(f"{item} dosnt exists in tuple")    
#Concatenate two tuples.
x=("sun","mon","tue","wed")
y=("thurs","fri","sat")
z=x+y
print(z)
#Repeat a tuple three times.
days=("sun","mon","tue","wed","thurs","fri","sat")
z=days*3
print(z)
#Find the length of a tuple.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(len(days))
#Convert a list into a tuple.
days=["sun","mon","tue","wed","thurs","fri","sat"]
convert=tuple(days)
print(convert)
#Convert a tuple into a list.
days=("sun","mon","tue","wed","thurs","fri","sat")
convert=list(days)
print(convert)
#Find the index of an element in a tuple.
days=("sun","mon","tue","wed","thurs","fri","sat")
print(days.index("wed"))
#Count occurrences of an element in a tuple.
days=("sun","fri","tue","sun","tue","fri","sun")
print(days.count("fri"))
#Create a nested tuple and access inner elements.
days=(1,2,3,(3,4,6,),9,(9,8,7),10)
print(days[5])
print(days[3][1])
#Check if all elements in a tuple are integers.
x=(1,2,3,4,5,6,7,8,9,10)
print(all(isinstance(item,int) for item in x))
#Unpack a tuple into variables.
data=(10,20,30,40)
a,b,c,d=data
print(a)
print(b)
print(c)
print(d)
#Swap values of two variables using a tuple.
a="divya"
b="chitti"
a,b=b,a 
print(a,b)
#Iterate through a tuple using a loop.
data=("divya","chitti","kanapala","vallabhapuram")
for item in data:
    print(item)
#Find the max and min values in a numeric tuple.
data=(10,20,30,40,50,60,70,80,90)
print(min(data))
print(max(data))
#Sort elements of a tuple (convert and sort).
data=(50,30,80,10,40)
print(sorted(data))
convert=sorted(data)
print(convert)
#Merge tuples of equal length into pairs.
tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
merged=tuple(zip(tuple1,tuple2))
print(merged)
#Create a tuple of even numbers using range().
even_numbers=tuple(range(0,20,2))
print(even_numbers)  

#Create a string with your name and print it.
str1="divya"
print(str1)
#Get the first character from the string.
print(str1[0])
#Get the last character from the string.
print(str1[4])
#Concatenate two strings.
str1="divya"
str2="chitti"
result=str1+str2
print(result)
#Repeat a string 3 times.
str1="chitti"
print(str1*3)
#Slice the first 5 characters.
str1="chittikanapala"
print(str1[:5])
#Reverse a string using slicing.
str1="chittikanapala"
print(str1[::-1])
#Check if a substring exists in a string.
str1="python programming language"
substring="language"
if substring in str1:
    print("substring found!!")
else:
    print("substring not found!!!")    
#Find the length of a string.
str1="chittikanapala"
print(len(str1))
#Convert string to uppercase.
str1="chittikanapala"
print(str1.upper())
#Convert string to lowercase.
str1="chittikanapala"
print(str1.lower())
#Capitalize the first letter.
str1="chittikanapala"
print(str1.capitalize())
#Convert a string to title case.
str1="chittikanapala"
print(str1.title())
#Remove leading spaces using lstrip().
str1="****chitti kanapala****"
print(str1.lstrip("*"))
#Remove trailing spaces using rstrip().
str1="****chitti kanapala****"
print(str1.rstrip("*"))
#Remove both ends' spaces using strip().
str1="****chitti kanapala****"
print(str1.strip("*"))
#Replace all spaces with underscores.
str1="    chitti kanapala    "
print(str1.replace(" ","_"))
#Count how many times a character appears.
str1="chitti kanapala"
z="a"
print(str1.count(z))
#Find index of a character using find().
str1="chitti kanapala"
char="k"
index=str1.find(char)
print(index)
#Use rfind() to find last occurrence.
str1="chitti kanapala"
z=str1.rfind("kanapala")
print(z)
#Use index() to find substring position.
str1="python programming language"
substring=str1.index("language")
print(substring)
#Split a string by spaces.
str1="python programming language"
x=str1.split(" ")
print(x)
#Join a list of words into a string.
list1=["python","programming","language"]
str1=" ".join(list1)
print(str1)
#Check if string starts with "Hello".
str1="hello, how are you?"
print(str1.startswith("hello"))
#Check if string ends with "world".
str1="hello world"
print(str1.endswith("world"))
#Check if a string is digit.
str1="2004"
print(str1.isdigit())
#Check if a string is alphabet.
str1="chitti"
print(str1.isalpha())
#Check if a string is alphanumeric.
str1="divya2004"
print(str1.isalnum())
#Get ASCII value of a character.
str1="c"
ascii_value=ord(str1)
print(ascii_value)                                                     
#Convert ASCII to character.
ascii_value=65
print(chr(ascii_value))
#Remove punctuation from string.
import string
text="hello, world! how's it going?"
text2=text.translate(str.maketrans('', '', string.punctuation))
print(text2)
#Swap case of all characters.
text="Hello World! Python"
print(text.swapcase())
#Count total words in a string.
str1="divya chitti kanapala"
x=str1.split()
count=len(x)
print(count)
#Count total sentences in a string.
text="hello world! Welcome to python programming. How are you doing? I hope you're learning python. Let's code more."

#Convert string to list of characters.
str1="chitti"
x=list(str1)
print(x)
#Convert list of characters to string.
list1=["c","h","i","t","t","i"]
str1=str(list1)
print(str1)
#Pad string to the left with * to length 10.
data="chitti"
x=data.rjust(10,"*")
print(x)
#Center align string using center().
text="chitti"
x=text.center(10,"*")
print(x)
#Format string with variables using f-string.
a="chitti"
b=25
print(f"my name is {a} and i am {b} years old")
#Use % operator to format a string.
a="divya"
b=21
print("my name is %s and i am %d years old." %(a,b))

#problems on sets()
#Create a set with integers and print it.
set1={1,2,3,4,5,6,7,8,9,10}
print(set1)
#Add a single item to a set.
sets={1,2,3,4,5,6}
sets.add("hi")
print(sets)
#Add multiple items to a set using update().
sets={1,2,3,4,5}
sets.update([6,7,8,9])
print(sets)
#Remove an element using remove().
sets={1,2,3,4,5,6,7,8,9}
sets.remove(6)
print(sets)
#Remove an element using discard().
sets={1,2,3,4,5,6,7,8,9}
sets.discard(4)
print(sets)
#Pop an item from a set and display it.
sets={1,2,3,4,5,6,7,8,9}
print(sets)
x=sets.pop()
print(sets)
print(x)
#Clear a set completely.
sets={1,2,3,4,5,6,7}
sets.clear()
print(sets)
#Check membership of an element in a set.
sets={1,2,3,4,5,6,7}
if 3 in sets:
    print("3 is in set")
else:
    print("3 is not in set")    
#Create union of two sets.
set1={1,2,3,4,5}
set2={6,7,8,9,10}
x=set1.union(set2)
print(x)
#Find intersection of two sets.
set1={1,2,3,4,5}
set2={3,5,8,9,10}
x=set1.intersection(set2)
print(x)
#Find the difference between two sets.
set1={1,2,3,4,5}
set2={3,5,8,9,10}
x=set1.difference(set2)
print(x)
#Find symmetric difference between sets.
set1={1,2,3,4,5}
set2={3,5,8,9,10}
x=set1.symmetric_difference(set2)
print(x)
#Check if one set is subset of another.
set1={3,5}
set2={3,5,8,9,10}
if set1.issubset(set2):
    print("set1 is a subset of set2")
else:
    print("set1 is not a subset of set2")    
#Check if one set is a superset of another.
set1={3,5}
set2={3,5,8,9,10}
if set2.issuperset(set1):
    print("set2 is superset of set1")
else:
    print("set2 is not a superset of set1")    
#Convert a list with duplicates into a set.
list1=[1,2,3,1,2,4,5,6,7]
set1=set(list1)
print(set1)
#Use set comprehension to create square numbers.
op={x**2 for x in range(1,10)}
print(op)
#Iterate over a set and print items.
set1={"divya","chitti","cryso","asha","sneha"}
for item in set1:
     print(item)
#Copy a set using copy().
set1={"divya","chitti","cryso"}
x=set1.copy()
print(x)
#Remove duplicates from a list using set().
list1=[1,2,3,1,2,4,5,6,7]
x=set(list1)
print(x)
#Use a set to store unique characters of a string.
str1="chitti"
x=set(str1)
print(x)
#Create an empty set and add elements one by one.
set1=set()
set1.add(10)
set1.add(20)
set1.add(30)
print(set1)
#Use a set in a loop to collect unique items.
x=[10,20,30,20,30,40,50]
y=set()
for num in x:
    y.add(num)
print(y)    
#Test if two sets are disjoint.
set1={1,2,3,4,5}
set2={6,7,8,9,10}
if set1.isdisjoint(set2):
    print("the sets are disjoint")
else:
    print("the sets are not disjoint")    
#Use frozenset and demonstrate immutability.
set1=frozenset([1,2,3,4,5,6,7,4,6])
print(set1)
#set1.remove(1)
#Convert tuple to set.
tuple1=("sun","mon","tue","wed")
set1=set(tuple1)
print(set1)
#Convert set to list.
set1={"divya","chitti","cryso"}
list1=list(set1)
print(list1)
#Merge multiple sets into one.
set1={10,20,30}
set2={40,50,60}
set3={70,80,90}
merged_set=set1.union(set2,set3)
print(merged_set)
#Filter a list using set membership.
list1=["apple","banana","mango","cherry"]
set1={"apple","cherry"}
x= [item for item in list1 if item in set1]
print(x)
#Find unique words in a sentence using set.
x="my name is divya!! i am from guntur.. my cource is python full stack"
words=x.split()
y=set(words)
print(y)
#Count unique vowels in a string.

#Get common elements from three sets.
set1={1,2,3,4,5}
set2={4,5,3,7,8}
set3={1,2,8,3,5}
x=set1.intersection(set2,set3)
print(x)
#Find non-overlapping items between two sets.
set1={1,2,3,4}
set2={3,4,5,6}
x=set1.symmetric_difference(set2)
print(x)
#Use set to find repeated items in a list.
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return duplicates
my_list = [1, 2, 3, 4, 2, 3, 5, 6, 1]
repeats = find_duplicates(my_list)
print("Repeated items:", repeats)
#Compare two sets and print differences.
set1={1,2,3,4,5}
set2={4,5,6,7}
diff1=set1-set2
print("items in set1 but not in set2:", diff1)
diff2=set2-set1
print("items in set2 but not in set1:", diff2)
difference=set1.symmetric_difference(set2)
print("items in either set but not both:", difference)
#Perform chained union of multiple sets.
set1={1,2,3}
set2={3,4,5}
set3={5,6,7}
result=set1.union(set2,set3)
print("chained union:",result)
#Check length of a set after each operation.
set1=set()
print("initial length:", len(set1))
set1.add(10)
print("length after adding 1st element:",len(set1))
set1.add(20)
print("length after adding 2nd element:",len(set1))
set1.add(30)
print("length after adding 3rd element:",len(set1))
#Use set to filter out special characters from a string.
str1="hello@# world!! welcome$%&*"
allowed_chars=set("abcdefghijklmnopqrstuvwxyz")
filtered_str="".join(ch for ch in str1 if ch in allowed_chars)
print("original:",str1)
print("filtered:",filtered_str)
#Use set to group users by unique roles.
users=[ 
    {"name":"divya","role":"admin"},
    {"name":"chitti","role":"editor"},   
    {"name":"cryso","role":"viewer"},
    {"name":"ashaa","role":"trainer"},
    {"name":"sneha","role":"trainee"}
]
x={user["role"] for user in users}
print("unique roles:",x)
#Find all even numbers from 1 to 50 using set.
even_numbers={num for num in range(1,51) if num%2==0}
print("even numbers from 1 to 50:",even_numbers)
#Combine numbers and letters into a single set.
letters=set("divyachitti")
numbers=set([1,2,3,4,5])
x=letters|numbers
print("combined set:",x)
#Find missing elements from a full range set.
list1={1,2,4,6,7}
full_range_set=set(range(min(list1),max(list1)+1))
set1=set(list1)
missing_elements=full_range_set-set1
print("missing_elements:",sorted(missing_elements))
#Compare performance of set vs list in membership tests. 

#Use set to validate inputs in a quiz app.
valid_choices={"A","B","C","D"}
print("Questions: What is the capital of France?")
print("A. Berlin")
print("B. Madrid")
print("C. Paris")
print("D. Rome")
user_answer=input("enter your answer (A/B/C/D):").strip().upper()
if user_answer in valid_choices:
    if user_answer == "C":
        print("Correct")
    else:
        print("Incorrect. The correct answer is C.")
else:
    print("Invalid input. please enter one of A,B,C or D.")            
#Compare two dictionaries by converting their keys to sets.
dict1={"a":1,"b":2,"c":3}
dict2={"b":4,"c":3,"d":5}
keys1=set(dict1.keys())
keys2=set(dict2.keys())
common_keys=keys1&keys2
unique_to_dict1=keys1-keys2
unique_to_dict2=keys2-keys1
all_keys=keys1|keys2
print("common keys:",common_keys)
print("unique to dict1:",unique_to_dict1)
print("unique to dict2:",unique_to_dict2)
print("All keys:",all_keys)
#Analyze word frequency using set and dict together.
text="apple orange banana apple mango banana apple"
words=text.split()
unique_words=set(words)
word_freq={}
for word in words:
    word_freq[word]=word_freq.get(word,0)+1
print("unique words:",unique_words)
print("word frequencies:")
if word in unique_words:
    print(f"{word}:{word_freq[word]}")    
#Identify duplicate words from a paragraph using set.
paragraph = "Python is easy to learn. Python is powerful and easy to use."
words = paragraph.lower().replace('.', '').split()
seen = set()
duplicates = set()
for word in words:
    if word in seen:
        duplicates.add(word)
    else:
        seen.add(word)
print("Duplicate words:", duplicates)
#Find if any letter is repeated in a string using set.
def has_repeated_letters(s):
    seen=set()
    for char in s:
        if char in seen:
           return True
        seen.add(char)
    return False
string="hello"
if has_repeated_letters(string):
    print("repeated letter found.")
else:
    print("all letters are unique")            
#Print ASCII codes of unique characters in a string.
text="hello world"
unique_chars=set(text)
for char in unique_chars:
    print(f"'{char}':{ord(char)}")
#Demonstrate set behavior with mutable and immutable elements.
valid_set={1,"apple",(2,3)}
print("valid set:",valid_set)
#Build a set from user input until 'stop' is entered.
user_inputs=set()
print("enter values (type 'stop' to finish):")
while True:
    value=input(">>").strip()
    if value.lower()=='stop':
        break 
    user_inputs.add(value)
print("\nunique inputs entered:")
print(user_inputs)    '''  

# problems on Dictionary 
#Create an empty dictionary and add some key-value pairs.
#Access the value of a specific key in a dictionary.
#Update the value of a key in a dictionary.
#Delete a key from a dictionary using del.
#Remove a key using pop().
#Use popitem() and explain its effect.
#Check if a key exists in a dictionary.
#Get all keys using keys() method.
#Get all values using values() method.
#Get all items (key-value pairs) using items().
#Iterate over keys and values in a dictionary.
#Use get() to safely access dictionary values.
#Merge two dictionaries using update().
#Use dictionary comprehension to create a squared dict.
#Create a dictionary from a list of tuples.
#Create a dictionary from two lists using zip().
#Count frequency of elements using a dictionary.
#Group items in a list using a dictionary.
#Find the key with the maximum value.
#Find the key with the minimum value.
#Remove all items from a dictionary.
#Copy a dictionary using copy().
#Sort dictionary by keys.
#Sort dictionary by values.
#Convert a dictionary to a list of tuples.
#Convert a list of tuples to a dictionary.
#Store nested dictionary data.
#Access values in a nested dictionary.
#Modify values in a nested dictionary.
#Check if dictionary is empty.
#Iterate over a nested dictionary.
#Delete a nested key in a dictionary.
#Track student scores using dictionary.
#Map cities to their country using dictionary.
#Reverse key-value pairs in a dictionary.
#Find common keys between two dictionaries.
#Merge dictionaries with overlapping keys.
#Remove keys with None values.
#Create a dictionary of vowel counts from string.
#Implement a simple word frequency counter.
#Create a dictionary from a string with index as keys.
#Replace specific values in a dictionary.
#Convert dictionary keys to uppercase.
#Compare two dictionaries for equality.
#Filter dictionary by values.
#Build a dictionary from user input until exit.
#Format a dictionary into readable text.
#Nest list inside dictionary and access values.
#Handle missing keys using defaultdict (optional).
#Create a dictionary of squares for numbers 1 to 10.

