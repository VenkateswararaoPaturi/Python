'''
Author: Venkat
Date: 24/09/2018
Script: Bank Account Details
Description: Receive bank name as commland line argument and customer choose Deposit or withdra.

'''
import sys

if(len(sys.argv)!=2):
 print("invalid arguments passed")
print("Welcome to",sys.argv[1], "bank") 
Usr_Det={ "Venkat":"Venkat123","Bindu":"Bindu123","Rams":"Rams123"}
print("Enter user name\n")
Usr_Nme=input()
print("Enter user password\n")
Usr_Pwd=input()

if(Usr_Nme in Usr_Det.keys()):
 print("user name is valid")
 if(Usr_Pwd==Usr_Det[Usr_Nme]):
  print("Login Sucess")
 else: 
  print("Invalid Password") 
  sys.exit[1]
else: 
 print("Login failed with invalid user ")
 sys.exit[1] 
print("Welcome to", Usr_Nme) 
Usr_Act={ "Venkat":8600152197,"Bindu":9550210273,"Rams":9492903394}
Acc_Det={ 8600152197:50000,9550210273:100000,9492903394:30000} 


Acct_Num=Usr_Act[Usr_Nme]
Acct_Bal=Acc_Det[Acct_Num]


print("usrname is %s \n account number is %d\n balance is %d \n"%(Usr_Nme,Acct_Num,Acct_Bal))

n = int(input("Enter your choice\n 1. Balance enquiry \n 2. Withdraw \n 3. Deposit \n"))

if n == 1:
 print("Balance is:", Acct_Bal)
elif n==2:
 wtr=int(input("Enter amount to withdra:"))
 if(Acct_Bal<wtr):
  print("Insufficient balance")
 else:
  print("Balance is:" ,Acct_Bal-wtr)
elif n==3:
 dep=int(input("Enter amount to deposit:"))
 print("Updated Balance is:" ,Acct_Bal+dep) 
else:
 print("Invalid Option")
 
print("Thanks for visiting ", sys.argv[1])
 
 


