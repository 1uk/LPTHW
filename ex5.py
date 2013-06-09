# variable definitions
name = 'Zed A. Shaw'
age = 35 # not a lie
height_inch = 74 # inches
height_cm = height_inch * 2.54
weight_pd = 180 # lbs
weight_kg = weight_pd * 0.45359237
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# printing all out
print "Let's talk about %s." % name
print "He's %d inches tall (%d cm)." % (height_inch, height_cm)
print "He's %r pounds heavy (%d kg)." % (weight_pd, weight_kg)
print "Actually that's not too heavy."
print "He's got %r eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
# calculating a little bit
print "If I add %d, %d, and %d I get %d." % (
        age, height_inch, weight_pd, age + height_inch + weight_pd)
