import os
import sys

def main():

	if len(sys.argv) == 2:

		if sys.argv[1] == 'learn':
			print("You are running PyThonOs in learn mode \n")
		elif sys.argv[1] == 'browse':
			print("You are running PyThonOs in browse mode \n")

		response = input('Select an item to learn from the course outline: ')
		
		if response  == '1':
			print("You have chosen to learn about the __file__ variable")
			print("You get the name of this script by printing the  __file__ variable: ", __file__)

		elif response  == '2':
			print("You have chosen to learn about the os.path.abspath() manipulation")
			print("The  full path to this script is: ", os.path.abspath(__file__))
			print("You get this by printing 'os.path.abspath(__file__)' " )

		elif response  == '3':
			print("You have chosen to learn about the os.path.basename() manipulation")
			print("The  basename of this script is: ", os.path.basename(os.path.abspath(__file__)))
			print("The basename is just the file name without the rest of the path.")
			print("You get this by printing 'os.path.dirname(os.path.abspath(__file__))' ")
		elif response == '4':
			print("The  directory containing this script is: ", os.path.dirname(os.path.abspath(__file__)))
			print("You get this by printing 'os.path.dirname(os.path.abspath(__file__))' " )
			print("Lets break it down from inside out")
			print("'os.path.abspath(__file__)' gives us: ", os.path.abspath(__file__))
			print("That is then passed as the argument to 'os.path.dirname()'")
			# to refactor to use a dictionary for dynamic selection 
	else:
		print("Use pythonos with arguments 'learn' or 'browse' ")

print("Welcome to PyThonOs 1.0")
print("------------------------")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("A simple python script I made for myself to understand the os.path manipulations")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print("Course Outline \n")

print("1. The __file__ variable \n")
print("2. os.path.abspath()  \n")
print("3. os.path.basename() \n")
print("4. os.path.dirname() \n")
print("5. os.path.exists() \n")

print("os.path.basename: ", os.path.basename(os.path.abspath(__file__)))
print("os.path.exists: ", os.path.exists(os.path.basename(os.path.abspath(__file__))))

print("The name of this module is", __name__)

if __name__ == '__main__':
	main()
else:
	print("It seems you are importing pythonos. To get full functionality you will need to run pythonos as a script")
	exit()
