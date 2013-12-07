def start_room():
    doors = 1,1,1,1
    print "You are in a white room with a black way on the ground."
    print_doors(doors)
    print "The way goes to every door and so builds a black cross on the white ground."
    print "You see also a sign with instructions on it."
    print "What do you do?"

    next = raw_input("> ")
    if ("left" in next):
        football_room()
    elif ("right" in next):
        pond_room()
    elif ("front" in next or "forward" in next):
        pc_room()
    elif ("read" in next or "instr" in next):
        instructions()
    else:
        print "I don't know what that means."

def print_doors(doors):
    print "There is a door",
    if (doors[0]):
        print "in front of you",
    if (doors[1]):
        print ", on the right",
#    if (doors[2]):             # actually you know the door you come from
#        print ", behind you",
    if (doors[3]):
        print "on the left",
    print "."

def dead(reason):
    print reason
    exit(0)

def welcomemsg():
    print "Welcome to the game !"
    print "This is an easy game, don't expect to much."

def start():
    welcomemsg()
    print "There is a great white wall with a black gate in front of you."
    print "You can't see the beginning and the end of the wall it seems to be endless."
    print "Do you enter the gate ? [Y/n]"

    next = raw_input("> ")
    if ("n" in next):
        dead("You wait outside the gate until you starve. Good job!")
    else:
        start_room()

start()
