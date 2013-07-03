from sys import argv

# myfunc(): adds to numbers together
def myfunc(n1, n2):
    print "%r + %r = %r" % (n1, n2, n1 + n2)

script, first, second = argv

print "Adding the two numbers from commandline together:"
myfunc(int(first), int(second))

print "Adding two other positive numbers:"
myfunc(20, 1)

print "Adding a negative and a positive number"
myfunc(4, -29)

print "Adding floating numbers"
myfunc(3.1, 9.543643753863643265437365)

print "STOP THATS ENOUGH !"
