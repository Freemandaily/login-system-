#Creating a login details
while True:
    user=input("Choose a username\n")
    #usernameinput must be  above 4 
    user_len=len(user)
    if user_len<=4:
        print('Error!Username letters must be greater than 4.TRY AGAIN')
        continue
    z=user[0] 
    y=123
    try:
        x=int(z)
        #comfiming that username dosent start with number
        if type(x)==type(y):
            print("Username shouldnt start with a number!TRY AGAIN")
            continue
    except:
        break
#Password must contain letters and numbers ; its length >=8
def password_accept():
   while True:
        global passkey
        passkey=input("Set password\n")
        pass_len=len(passkey)
        if pass_len<8:
            print("Error!Your Password Must Be Greater Than 7!:TRY AGAIN")
            continue
        if pass_len>=8:
            break
   y=0
   z=0
#checking if the password contain letters  and numbers
   for i in passkey: 
       try:
          x=int(i)
          y=y+1
          if y==pass_len:
              print("Error!Password must contain numbers and letters: TRY AGAIN")
              password_accept()
       except: 
           z=z+1
           if z==pass_len:
                print("Error!Password must contain letters and numbers: TRY AGAIN")
                password_accept()
password_accept()
#password reset processing function
def password_reset():
   while True:
        global passkey
        comf_username=input("Enter your username\n")
        if comf_username!=user:
            print(" Error! Username not in our system: TRY AGAIN")
            continue
        new_passkey=input("Set new password\n")
        comf_passkey=input("Comfirm your new password\n")
        pass_len=len(new_passkey)
        if pass_len<8:
            print("Error!Your Password Must Be Greater Than 7:TRY AGIAN")
            continue
        if  comf_passkey!=new_passkey:
            print('Error!:Password comfirmation error: TRY AGAIN')
            continue
        else:
            global incorrect_user
            global incorrect_pass
            global passkey
            incorrect_user=0
            incorrect_pass=0
            passkey=comf_passkey
            break
   y=0
   z=0
   for i in passkey:
       try:
          x=int(i)
          y=y+1
          if y==pass_len:
              print("Error!Password must contain numbers and letters: TRY AGAIN")
              password_reset()
       except: 
           z=z+1
           if z==pass_len:
                print("Error!Password must contain letters and numbers:TRY AGAIN")
                password_reset()
   print('You Can Login With Your New Pasword Now')

#loging in with user details
incorrect_user=0
incorrect_pass=0
while True:
#if user input incorrct detail more than 2 times password_reset() will trigger
    if incorrect_user>1 or incorrect_pass>1:
        print("You Can Reset Your Password Now")
        password_reset()
    print("TIME TO LOGIN")
    username=input("Enter your username\n")
    password=input("Enter your password\n")
    if username!=user:
        print("Error!Username incorrect:TRY AGAIN")
        incorrect_user=incorrect_user+1
        continue
    if password!=passkey :
        print("Error!Incorrect password:TRY AGAIN")
        incorrect_pass=incorrect_pass+1
        continue
    else:
        print("WELCOME",user)
        break
