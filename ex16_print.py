# importing argv module from sys
from sys import argv

# getting command line argument
script, filename = argv

# opening file
txtfile = open(filename, 'r')
# printing the content of the file
print txtfile.read()
# closing the file
txtfile.close()
