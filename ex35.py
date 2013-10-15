from sys import exit

layer = 0

def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    if next.isdigit():
        how_much = int(next)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bad guy!")

def pc_room():
    print "There is a running computer in this room."
    print "On the left side, you see a great door."
    print "What do you do ?"
    next = raw_input("> ")
    if "door" in next:
        gold_room()
    elif "computer" in next or "pc" in next:
        computer()
    elif "back" in next:
        dead("The bear jumps at you and eats you at one swallow.")
    else:
        dead("Learn to play.")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input(">")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            pc_room()
        else:
            print "I got no idea what that means."


def ghost_room():
    print "Here you see a ghost."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    print "Or do you fight against the ghost (are you a real man) ?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    elif "fight" in next or "ghost" in next or "yes" in next or "man" in next:
        trapdoor()
    else:
        ghost_room()

def trapdoor():
    print "A trapdoor opens under you, you fall down into another room"
    print "The looks very empty and dull."
    print "There is a passage on every side of the room, where do you go next ?"
    print "Left, right, or straight on ?"
    raw_input("> ")
    endless_room()

def endless_room():
    print "This room looks just like the one you come from."
    print "There is also a passage on every side of the room, where do you go next ?"
    print "Back, left, right or straight ahead ?"
    raw_input("> ")
    endless_room()

def computer():
    global layer
    print "There is a computer game opened."
    print "It seems to be a text adventure game."
    print "You read the text...\n"
    layer += 1
    start()


def dead(why):
    global layer
    print why, "Good job!"
    if (layer > 0):
        layer -= 1
        print "You leave the computer and look around."
        pc_room()
    else:
        exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        ghost_room()
    else:
        dead("You stumble around the room until you starve.")

start()
