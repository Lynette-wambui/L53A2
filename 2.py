#create a new file
new_file = open('file.txt', 'x')
new_file.close()

#check if a file exists
import os
print("Checking if my_mainfile exists or not..")
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:
    print("The file does not exist")

#create a new file if it doesn't 
my_file = open("main.txt", "w")
my_file.write("Hi! My name is Lynette Wambui.")
my_file.close()