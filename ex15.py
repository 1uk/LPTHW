# importing argv from sys module
from sys import argv

# getting the filename through the command line
script, filename = argv

# opening the file filename
txt = open(filename, 'r')

# printing simple text
print "Here's your file %r:" % filename
# printing the txt variable with no arguments for read()
print txt.read()

# closing the file filename again
txt.close()

# printing simple text
print "Type the filename again:"
# input filename again
file_again = raw_input("> ")

# opening the file file_again
txt_again = open(file_again)

# printing text_again without arguments
print txt_again.read()

# closing the file file_again again
txt_again.close()
