print("Bank of codédex")
pin = int(input("Enter your pin : "))
while pin != 1234 :
	pin = int(input("Invalid pin !. Please enter a valid pin : "))
if pin == 1234:
	print("Correct pin")
print("Welcome to your account")