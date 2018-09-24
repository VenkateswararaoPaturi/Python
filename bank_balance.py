'''
script name : login.py
Author : phani
Date : 23/09/2018
Description : login details validation

'''
import sys


if(len(sys.argv) != 2):
 print("invalid arguments")
 sys.exit(1)

bank_nm = sys.argv[1]

print("welcome to ",bank_nm)



usrs_dtls = {'HDFC001':'HDFC_PWD_001','HDFC002':'HDFC_PWD_002'}

usr_nm = input("Enter username\n")
pwd = input("Enter password\n")

usrs = usrs_dtls.keys()

if( usr_nm in usrs):
 if(pwd == usrs_dtls[usr_nm]):
  print("login success")
 else:
  print("invalid password")
  sys.exit(1)
else:
 print("invalid user")
 sys.exit(1)


print("welcome Mr.",usr_nm)

usr_act = {'HDFC001':2312345,'HDFC002':4563455}
act_bal = {2312345:20000,4563455:30000}

acct_nbr = usr_act[usr_nm]
avail_bal = act_bal[acct_nbr]

print("usrname is %s account number is %d and balance is %d"%(usr_nm,acct_nbr,avail_bal))

n = int(input("Enter your choice\n 1. Balance enquiry \n 2. Withdraw \n 3. Deposit \n"))

if n==1:
 print("Avaliable balance is",avail_bal)
elif n==2:
 wdr_amt = int(input("Enter the amount to with draw\n"))
 if(wdr_amt < avail_bal):
  print("The available balance is",avail_bal-wdr_amt)
 else:
  print("insufficient balance")
 
elif n==3:
 dpst_amt = int(input("Enter the amount to deposit"))
 print("The avaliable balance is\n",avail_bal+dpst_amt)
else:
 print("invalid choice")

print("Thanks for visiting ",bank_nm)