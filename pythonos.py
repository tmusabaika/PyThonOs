import  os
print("Welcome to PyThonOs 1.0")
print("------------------------")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("A simple python script I made for myself to understand the os.path manipulations")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("The  directory containing this script is: ", os.path.dirname(os.path.abspath(__file__)))
print("The name of this script is: ", __file__)
print("os.path.basename: ", os.path.basename(os.path.abspath(__file__)))
print("os.path.exists: ",os.path.exists(os.path.basename(os.path.abspath(__file__))))


