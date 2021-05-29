granted = False
def grant():
    global granted
    granted = True
def login(name,password):
    success = False
    file = open("user_detail.txt","r")
    for i in file:
         a,b = i.split(",")
         b = b.strip()
         if(a==name and b==password):
             success = True
             break
    file.close()
    if(success):
        print("Login Successful")
        grant()
    else:
        print("wrong user name or password")
        
def register(name,password):
    file = open("user_detail.txt","a")
    file.write("\n"+name+","+password)
    grant()
def access(option):
    global name
    if(option=="login"):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        register(name,password)

def begin():
    global option
    print("welcome to Victor's programming club")
    option = input("Login or Register (Login,Reg): ")
    if(option!="login" and option!="reg"):
        begin()
        
begin()
access(option)

if(granted):
    print("Welcome to Victor's Programming club")
    print("### USER DETAILS ###")
    print("Username: ",name)


    
