# importing the argv module from sys
from sys import argv

# getting the command line arguments
script, filename = argv

# printing some text
print "We're going to erase %r." % filename
print "If you do not want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# asking for confirmation
raw_input("?")

# opening the file defined on command line
print "Opening the file..."
target = open(filename, 'w')

# following not necessery, open() does truncate
# truncating the file
#print "Truncating the file..."
#target.truncate()

# printing
print "Now I'm going to ask you for three lines."

# input some text from command line
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# printing
print "I'm going to write these to the file."

# writing them with newlines after to the file
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

# closing the file
print "And finally, we close it."
target.close()
