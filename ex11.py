print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "Where do you come from ?",
home = raw_input()
print "What's your favorite food ?",
food = raw_input()
print "What's your name ?",
name = raw_input()
print "The answer is 42, what was the question ?"
question = raw_input()

print "So, you're %r old, %r tall and %r heavy," % (
        age, height, weight),
print "Your name is %r, you like %r and you're coming from %r" % (
        name, food, home)
