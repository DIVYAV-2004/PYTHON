#creating single or static object from class
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
obj1=person("chittii",25)
print(obj1.name)
print(obj1.age)
# creating dynamic or multiple objects from class
class person:
    def __init__(self,name,gender,age):
        self.name=name
        self.gender=gender
        self.age=age
obj_chitti=person("chitti","male",25)
obj_divya=person("divya","female",21) 
print(obj_chitti.name)
print(obj_chitti.gender)
print(obj_chitti.age)
print(obj_divya.name)  
print(obj_divya.gender)
print(obj_divya.age)   
#creating dynamic objects
class Application:
    def __init__(app,name,color,usage):
        app.name=name
        app.color=color
        app.usage=usage
    def purpose(self):
        print("social media purpose")   
insta=Application("instagram","pink","entertainment")   
zomato=Application("zomato","red","food") 
rapido=Application("rapido","yellow","travelling")
print(insta.name)  
print(insta.color)
print(insta.usage)
insta.purpose()     
print(zomato.name)  
print(zomato.color)
print(zomato.usage)  
zomato.purpose()   
print(rapido.name)  
print(rapido.color)
print(rapido.usage)
rapido.purpose()     

class Application:
    def __init__(app,name,color,usage):
        app.name=name
        app.color=color
        app.usage=usage
    def purpose(self,app_name,purpose):
        print(f"{app_name} is used for {purpose}")   
insta=Application("instagram","pink","entertainment")   
zomato=Application("zomato","red","food") 
rapido=Application("rapido","yellow","travelling")
print(insta.name)  
print(insta.color)
print(insta.usage)
insta.purpose("instagram","socialmedia")     
print(zomato.name)  
print(zomato.color)
print(zomato.usage)  
zomato.purpose("zomato","food")   
print(rapido.name)  
print(rapido.color)
print(rapido.usage)
rapido.purpose("rapido","travelling") 

class bankaccount:
    def __init__(acnt,name,email,phno,balance):
        acnt.name=name
        acnt.email=email
        acnt.phno=phno
        acnt.balance=balance   
    def deposit(acnt,d_amnt):
        acnt.balance+=d_amnt  
    def withdraw(acnt,w_amnt):
        acnt.balance-=w_amnt 
    def checkbalance(acnt):
        print(acnt.balance)     
chitti_acnt=bankaccount("chitti","chitti@gmail.com","6305078330","50000")
chitti_acnt.checkbalance()
print(chitti_acnt.name)  
print(chitti_acnt.email)
print(chitti_acnt.phno)
print(chitti_acnt.balance)
chitti_acnt.deposit(10000)
chitti_acnt.checkbalance()
chitti_acnt.withdraw(20000) 
chitti_acnt.checkbalance()   



import random 
class BANK:
    T_Holders=[]
    def Create_New_Account(self):
        H_Details={}
        data=random.randint(100000000000,999999999999)
        H_Details["H_name"]=input("Enter The Name:")
        H_Details["Mobile No"]=input("Enter Mobile Number:")
        H_Details["Aadhar No"]=input("Enter Aadhar Number:") 
        H_Details["Account_Number"]=data
        n1=input("Select Type of Account Saving/Zero.......")
        while True:
            if n1=="Saving":
                n2=int(input("Deposite 1000 rupees....."))
                if n2==1000:
                    H_Details["Balance"]=n2
                    break
                else:
                    print("Deposite 1000 rupees....")
            elif n1=="Zero":
                n3=int(input("Deposite 500 rupees..."))
                if n3==500:
                    H_Details["Balance"]=n3
                    break
                else:
                    print("Deposite 500 rupees...")
        BANK.T_Holders.append(H_Details)
        print(BANK.T_Holders)  

obj=BANK()
obj.Create_New_Account()                     



import random
class bank:
    t_holders=[]
    def create_new_account(self):
        h_details={}
        data=random.randint(100000000000,999999999999)
        h_details["h_name"]=input("enter the name:")
        h_details["mobile no"]=input("enter mobile number:")
        h_details["aadhar no"]=input("enter aadhar number:")
        h_details["account_no"]=data
        n1=input("select type of account saving/zero:")
        while True:
            if n1=="saving":
                n2=int("deposite 1000 rupees...")
                if n2==1000:
                    h_details["balance"]=n2
                    break
                else:
                    print("deposite 1000 rupees:")
            elif n1=="zero":
                n3=int("deposite 500 rupees:")
                if n3==500:
                    h_details["balance"]=n3
                    break
                else:
                    print("deposite 500 rupees:")
        bank.t_holders.append(h_details)
        print(bank.t_holders)  
obj=bank()
obj.create_new_account()                          