from sys import argv

script, name = argv

age = int(raw_input("Hey %s, how old are you ? " % name))
hobby = raw_input("So you're %d years old and whats your hobby ? " % age)
print "Goodbye %r year old %s, who likes %s." % (
    age, name, hobby)
