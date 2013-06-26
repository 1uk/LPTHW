# importing some modules
from sys import argv
from os.path import exists

# getting command line arguments
script, from_file, to_file = argv

# reading the input file
indata = open(from_file, 'r').read()

# printing some stuff
print "%r exists: %s" % (to_file, exists(to_file))
print "Copying from %s (%d bytes) to %s" % (from_file, len(indata), to_file)

# writing to the output file
open(to_file, 'w').write(indata)

# success report
print "Alright, all done."
