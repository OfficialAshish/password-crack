import time
users = {"root": {
        "password": "starting_assgn"} }

# Register
def register():
    while True:
        username = input("New username: ")
        if len(username) == 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    	
    with open('userdata.txt' , 'a+') as apr:
    	apr.write(username + ',' + password)
    	apr.write('\n')
    time.sleep(1)
    print("Account has been created")
    
#login authorization
def login_auth(username,password):
	
	data_file=open('userdata.txt' , 'r' )
	strg=' '
	while strg:
		
		lst_d=data_file.readline()
		if lst_d =='':
			return False
		lst=lst_d.split(',')
		lst[1]=lst[1].rstrip('\n')
		if lst[0] == username and lst[1]== password:
			return True

# Login
def login():
    while True:
        username = input("Username: ")
        if len(username) ==0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if len(password) == 0:
            print("Password can't be blank")
        else:
            break

    if login_auth(username, password):
        return session(username)
    else:
        print("Invalid username or password")


# On exit
def exit():
	print("Shutting down...")
	time.sleep(1)
	
# On start
def start():
	print("Welcome to the system. Please register or login.")
	print("Options: register | login | exit")
	while True:
		option = input("> ")
		if option == "login":
			login()
		elif option == "register":
			register()
		elif option == "exit":
			exit()
			break
		else:
			print(option + " is not an option")
        
# User session
def session(username):
    print("Welcome to your account " + username)
    print("Option:  logout")
    while True:
        option = input(username + " > ")
        if option == "logout":
            print("Logging out...")
            break

