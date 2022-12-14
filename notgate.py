def notgate(A):
    if A == 1:
        return 0
    else:
        return 1


print("NOT Truth Table")
print("|A|Res\t|")
A = 1
res = notgate(A)
print("|" + str(A) + "|" + str(res) + "\t|")
A = 0
res = notgate(A)
print("|" + str(A) + "|" + str(res) + "\t|")
