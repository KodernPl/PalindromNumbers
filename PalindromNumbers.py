# Palindrom finder
import time

def check_if_palindrom(number):
    """
    Find if number is Palindrom
    @param number - int
    @return boolean
    """
    if(str(number)==reverse(str(number))):
        return True
    return False

def reverse(text):
    """
    Text reverse
    @param text - input text
    @return reverser text
    """
    text = str(text)
    if len(text) <= 1:
        return text
    return reverse(text[1:]) + text[0]

def try_to_make_palindrom(number):
    """
    Palindrome Making
    @param number - number from wihich will be trying to make palindrom
    @return palindrom or error message
    """
    start_time = time.clock()  
    while True:
        if(check_if_palindrom(number)):
            break
        elif(time.clock() - start_time > 5):  #Time for making palindrome 5s
            return "End of time for making palindrom from given number"
        else:
            number = number + int(reverse(number))
    return number

#main
lista = []

try:
	low_range = int(input("Enter the lower limit: "))
	high_range = int(input("Enter the upper limit: "))
	for x in range(low_range,high_range):
		lista.append((x,try_to_make_palindrom(x)))
	print(lista)
except Exception as e:
	print(e)

try:
	input("Press Enter key to continue...")
except:
	pass

