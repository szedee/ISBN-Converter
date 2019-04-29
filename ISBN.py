while True:
	
	ProductID = raw_input("Enter the 12 digit ProductID #: ") #get user input
	newProductID = ProductID.replace("-", "") # remove hyphen
	
	if len(newProductID) != 12 or newProductID[:3] not in ("978"): #check length of input, and must start with 978
		print("You did not enter a 12 digit # starting with 978. Please enter a 12 digit number: ")
	
	else:
		print("Valid ProductID\n") #valid ID message
		break

	

#print(newProductID) #to check if the ProductID is valid
newProductID = newProductID[3:] #remove 978 prefix
#print(newProductID) #to check the 9 digit number w/o prefix

checkSum = 0 #initialise
for i in range(len(newProductID)): #for loop for range with length of newProductID
	#sum the numbers iteratively while going down the index
	checkSum = sum(int(newProductID[i])*(10 - i) for i in xrange(9))
	checkSum %= 11 #check if sum is mod 11
	digit = 11 - checkSum #nearest next digit that is to be appended at the end of ISBN10
	
	if digit == 10: #digit 10 will return a "X"
		digit = "X"
	elif digit == 11: #digit 11 will return a "0"
		digit = 0
	else:
		digit == int(ProductID[-1]) #insert the new number at -1 position

newProductID = str(newProductID)+str(digit) #append the 2 numbers together
print("Your 10 digit ISBN is " + newProductID) #print new ISBN10	
