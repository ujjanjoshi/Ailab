def orgate(A, B):
    if A == 0 and B == 0:
        return 0
    else:
        return 1


print("OR Truth Table")
print("|A|B|Res|")
A = 1
B = 1
res = orgate(A, B)
print("|" + str(A) + "|" + str(B) + "|" + str(res) + "\t|")
A = 1
B = 0
res = orgate(A, B)
print("|" + str(A) + "|" + str(B) + "|" + str(res) + "\t|")
A = 0
B = 1
res = orgate(A, B)
print("|" + str(A) + "|" + str(B) + "|" + str(res) + "\t|")
A = 0
B = 0
res = orgate(A, B)
print("|" + str(A) + "|" + str(B) + "|" + str(res) + "\t|")
