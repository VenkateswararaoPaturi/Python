import sys

Bank_Name = sys.argv[1]
print("Welcome to",Bank_Name)

user_dt = {'HDFC_001':'HDFC_PWD_001','HDFC_002':'HDFC_PWD_002'}

User_Name= input("Enter user name :\n")
password= input("Enter password :\n")

#print("User name is:",User_Name )
#print("Password Is:", password)

#Users=user_dt.keys()
#print(Users)
if (User_Name in user_dt.keys()):
  if(password==user_dt[User_Name]):
   print("login success")
  else:
   print("invalid password")
  sys.exit(1)
else:
  print("invalid user")
  sys.exit(1)
print("welcome Mr.",user_name)
	