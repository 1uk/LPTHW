# defining x (string with included integer)
x = "There are %d types of people." % 10
# defining binary (string)
binary = "binary"
# defining do_not (string)
do_not = "don't"
# defining y (string with included strings which have integers included)
y = "Those who know %s and those who %s." % (binary, do_not)    # here's a string inside a string

# printing the string x out
print x
# printing the string y out
print y

# printing a string with %r included string
print "I said: %r." % x    # here's a string inside a string
# printing a string with %s included string
print "I also said: '%s'." % y    # here's a string inside a string

# defining hilarious
hilarious = False
# defining joke_evaluation (string with %r included variable)
joke_evaluation = "Isn't that joke so funny?! %r"

# printing the string joke_evaluation with %r included variable hilarious
print joke_evaluation % hilarious    # here's a string inside a string

# defining w (string)
w = "This is the left side of..."
# defining e (string)
e = "a string with a right side."

# printing the string w and the string e out
print w + e
