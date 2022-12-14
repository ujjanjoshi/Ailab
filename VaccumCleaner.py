def process(Loc, Loc2, other_room_status, cost):
    print("Vacuum is placed in Location " + Loc)
    print("Location " + Loc + " is dirty")
    print("Cost for CLEANING " + Loc + " = 1")
    print("Location " + Loc + " has been cleaned")
    cost = cost + 1
    if other_room_status == "1":
        print("Location " + Loc2 + " is Dirty")
        print("Moving left/right to Location " + Loc2)
        print("Cost for moving left/right = 1")
        cost = cost + 1
        print("Cost for CLEANING " + Loc2 + " = 1")
        cost = cost + 1
        print("Location " + Loc2 + " has been cleaned")
    print("Goal Required:{A:'0', B:'0'}")
    print("Performance Measurement: " + str(cost))


print("* Suppose we have 2 rooms connected which is A and B")
print("* Action =(only 0 and 1) 0 means clean and 1 means dirty")
Loc = input("Location of a vacuum(A/B):")
if Loc == "A":
    Loc2 = "B"
else:
    Loc2 = "A"
status = input("Status of room " + Loc + ":")
cost = 0
other_room_status = input("Status of another room :")
print("Goal Required:{A:'0', B:'0'}")
if status == "1":
    process(Loc, Loc2, other_room_status, cost)
else:
    print("both of rooms are cleaned")
