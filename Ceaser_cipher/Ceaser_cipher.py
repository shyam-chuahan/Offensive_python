
def encrypt():   #encryption function defination
	flag = 0	#flag variable declaration
	text = input("Enter Text you want to encrypt: ") #taking input of plain text from user
	length = len(text) 	#determining length of input
	enc = '' 	#encryption text variable declaration

	for i in range(0,length):   #loop until last character of plain text
		temp = text[i]		#storing character in temp variable
		if(temp.islower()):	#checking if character is lower case
			enc += chr((((ord(temp) - 94)%26)+97))		#encryting text by adding 3 to it
		elif(temp.isupper()):	#checking if character is upper case
			enc += chr((((ord(temp) - 61)%26)+64))		#encryting text by adding 3 to it
		elif(temp == " "):	#checking if character is space
			enc += " "      #adding space to encrypted text
		else:
			print("Error!!") 	#other than character(e.g. digits or special characters) encountered & printing error message
			flag = 1		#setting up flag to 1
			break			#breaking the loop

	if(flag == 0):		#checking if error occured or not 
		print("Encrypted Text is : ",enc)	#no errors so printing the encrypted text
	else:	#error encountered
		pass 	#error message is alrady printed so do nothing
	


def decrypt():		#decryption function defination
	flag = 0		#flag variable declaration
	text = input("Enter Text you want to decrypt: ")	#taking input of cypher text from user

	length = len(text)	#determining length of input
	dec = ''		#decryption text variable declaration

	for i in range(0,length):	#loop until last character of plain text
		temp = text[i]		#storing character in temp variable
		if(temp.islower()):		#checking if character is lower case
			dec += chr((((ord(temp) - 100)%26)+97)) 	#decryting text by subtracting 3 from it
		elif(temp.isupper()):		#checking if character is upper case
			dec += chr((((ord(temp) - 68)%26)+65))		#decryting text by subtracting 3 from it
		elif(temp == " "):		#checking if character is space
			enc += " "		#adding space to decrypted text
		else:
			print("Error!!")	#other than character(e.g. digits or special characters) encountered & printing error message
			flag = 1		#setting up flag to 1
			break			#breaking the loop

	if(flag == 0):		#checking if error occured or not 
		print("decrypted Text is : ",dec)		#no errors so printing the decrypted text
	else:			#error encountered
		pass		#error message is alrrady printed so do nothing
	


if __name__ == '__main__':	#checking if program is running as main program
	choice = 1	#initializing choice variable
	while(choice != 3):		#running loop until user chooses to exit by presssing 3
		choice = int(input("1. For encryption \n2. For decryption \n3. For exit\n Enter your Choice :"))	#user input for choice where 1 is encryption 2 is decryption and 3 is exit
		if(choice == 1):	#choice 1
			encrypt()	#function call to encrypt
		elif(choice == 2):	#choice 2
			decrypt()	#function call to decrypt
		elif(choice == 3):	#choice 3
			print("You choose to exit")	#displaying exit message
			exit(0)		#exiting with no errors
		else:		#unknown choice
			print("Wrong choice !")		#displaying wrong choice message and running loop again
	
