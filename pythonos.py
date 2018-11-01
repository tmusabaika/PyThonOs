import os
import sys

def main():

	if len(sys.argv) == 2:

		if sys.argv[1] == 'learn':
			print("You have chosen learn mode")

		if input('Select an item to learn from the course outline: ') == '1':
			print("You have chosen to learn about the __file__ variable")
			# Use a dictionary for dynamic selection 
	else:
		print("Invalid \# of arguments")

print("Welcome to PyThonOs 1.0")
print("------------------------")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("A simple python script I made for myself to understand the os.path manipulations")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print("Course Outline \n")

print("1. The __file__ variable \n")

print("The  directory containing this script is: ", os.path.dirname(os.path.abspath(__file__)))
print("The name of this script is: ", __file__)
print("os.path.basename: ", os.path.basename(os.path.abspath(__file__)))
print("os.path.exists: ", os.path.exists(os.path.basename(os.path.abspath(__file__))))

if __name__ == '__main__':
	main()
