print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away. What do you do?" % bear
        print "1. Take the cake."
        print "2. Follow the bear."

        follow = raw_input("> ")

        if follow == "1":
            print "You take the squished cheese cake. What do you do?"
            print "1. Eat the cake."
            print "2. Follow the bear."

            cake = raw_input("> ")

            if cake == "1":
                print "Yuck! It tastes terrible. You die from food poisoning."
            elif cake == "2":
                print "You fall into a hole and die."

        elif follow == "2":
            print "You run after the bear. You fall into a hole and die."

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothepins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
