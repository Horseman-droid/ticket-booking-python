import json
import getpass
user=[]
def General_instruction():
    print('''\n========Some instruction========
1.0 As per Government Instruction All the seats are Non A.C
2.0 Reservation allotement criteria
2.1-students 40%
2.2-Government employee 35%
2.3-Others 25%, 
''')

def pnr():
    print('Your PNR status is t2')

def booking():
    i=0
    name2=[]
    agel=[]
    sexl=[]
    name=input('Enter your Name :')
    name2.append(name)
    age=int(input('Enter your Age :'))
    agel.append(age)
    sex=input('Male or Female :')
    sexl.append(sex)
    print('Ticket : ',1)
    print('Name : ', name2[0])
    print('Age  : ', agel[0])
    print('Sex : ',sexl[0])
    print('Ticket Booked')

def create_account():
	print("\n-----CREATE ACCOUNT-----")
	username = input("USERNAME: ")
	password = getpass.getpass(prompt='PASSWORD: ')
	with open('assets/user_accounts.json', 'r+') as user_accounts:
		users = json.load(user_accounts)
		if username in users.keys():
			print("An account of this Username already exists.\nPlease enter the login panel.")
		else:
			users[username] = [password]
			user_accounts.seek(1)
			json.dump(users, user_accounts)
			user_accounts.truncate()
			print("Account created successfully!!!")

def login():
	print('\n-------LOGIN PANEL -------')
	username=input("USERNAME: ")
	password=getpass.getpass(prompt='PASSWORD: ')
	with open('assets/user_accounts.json', 'r') as user_accounts:
		users=json.load(user_accounts)
	if username not in users.keys():
		print("An account of that name doesn't exist.\nPlease create an account first.")
	elif username in users.keys():
		if users[username][0]!=password:
			print("Your password is incorrect.\nPlease enter the correct password and try again.")
		elif users[username][0]==password:
			print("You have successfully logged in.\n")
			user.append(username)
			user.append(users[username][1])
def logout():
    user=[]
    print("You have been logged out successfully.")
		
if __name__=='__main__':
    choice=0
    while choice!=1:
        print('Welcome to ticket booking system')
        print(' *===========================*')
        print('1. General instruction')
        print('2. create account')
        print('3. login')
        print('4. ticket booking')
        print('5. pnr')
        print('6. logout')
        print('7. Exit')
        choice=int(input('enter your choice'))
        if choice==2:
            create_account()
        elif choice==3:
            login()
        elif choice==6:
            logout()
        elif choice==4:
            booking()
        elif choice==7:
            break
        elif choice==5:
            pnr()
        elif choice==1:
            General_instruction()
        else:
            print('use valid key')


            
                   

                
                
                
