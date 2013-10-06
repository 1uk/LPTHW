def myrange(start, end, step):
    arr = []
    for i in range(start, end, step):
        print "At the top i ist %d" % i
        arr.append(i)

        print "Numbers now: ", arr
        print "At the bottom i is %d" % i

    return arr

from sys import argv

script, first, second, third = argv

numbers = myrange(int(first), int(second), int(third))

print "The numbers: "

for num in numbers:
    print num
