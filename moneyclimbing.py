def monkeymove(loc, initalpos, count):
    if count == 0:
        if loc == "L":
            print("Monkey move to left")
            initalpos = "boxstick"
            count = count + 1
        if loc == "R":
            print("Warning the monkey is in wrong direction please start again!!")
            initalpos = ""
            count = 0
    if initalpos == "boxstick":
        temp = ""
        finalpos = ""
        while finalpos != "complete":
            loc1 = input("where sould the monkey go??")
            loc1 = loc1.upper()
            if loc1 == "U":
                print("Monkey climb the box grab the stick and hit the banana and got it!!")
                count = count + 1
                finalpos = "complete"
            elif loc1 == "R" and temp == "G":
                print("Monkey move to right and the postion of monkey is below the banana.")
                count = count + 1
            elif loc1 == "R":
                print("Monkey move to right")
                print("There contains a box that also contain stick on top")
                count = count + 1
            elif loc1 == "L":
                print("Monkey move to left")
                count = count + 1
            elif loc1 == "G":
                print("Monkey grab the box that also contain stick on top")
                temp = "G"
                count = count + 1
            elif loc1 == "RE":
                print("Monkey release the box that also contain stick on top")
                count = count + 1
        print("The total cost = " + str(count))


print("Scenario: There is a monkey in the room where a bunch of bananas are hanged at the centre of the ceiling."
      "\nBoxes and a stick are available in the room.To reach the banana,the monkey needs to climb the box and reach the banana with a stick."
      "\n(For the movement of monkey there consist Left(L),Right(R),Up(U),Grab(G),Release(Re))")
count = 0
intialpos = ""
Loc = input("where sould the monkey go??")
monkeymove(Loc.upper(), intialpos, count)
