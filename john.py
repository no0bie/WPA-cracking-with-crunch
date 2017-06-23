import os, time

n = ["n", "no"]
y = [" y","yes"]
e= (",'()")

def J(a):
	lis = []
	global n, y, e
	if a in n:
		os.system("clear")
		w = input("Want to use a wordlist ")
		while w not in n and w not in y:
			w = input("Please input yes or no ")
		if w in y:
			w = input("Type the wordlist name include file extension ")
			#check if file exists here
			#if file != exist:
				#print(file doesnt exist... Existing)
				#time.sleep(2)
			s = input("Want to add a session name ")
			while s not in n and s not in y:
				s = input("Please input yes or no ")
			if s in y:
				s = input("Enter desired session name ")
				command = " john -w ",w," --session-name=",s," ",n1
				for l in command:
					if l not in e:
						lis.append(l)
				os.system((str(''.join(lis))))
			else:
				command = "john -w ", w," ",n1
				for l in command:
					if l not in e:
						lis.append(l)
				os.system((str(''.join(lis))))
		else:
			command = "john ", n1
			for l in command:
					if l not in e:
						lis.append(l)
			os.system((str(''.join(lis))))
	else:
		r = input("Type the session you want to recover ")
		command = "john --recover"
		#TODO find out how to recover with john
		

def s():
	n1 = input("Do you want to recover a session ")
	while n1 not in n and n1 not in y:
		n1 = input(" Please input yes or no ")
	J(n1)
	
s()