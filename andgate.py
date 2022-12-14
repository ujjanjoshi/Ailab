def andgate(A,B):
    if A==1 and B==1:
        return 1
    else:
        return 0


print("AND Truth Table")
print("|A|B|Res|")
A=1
B=1
res=andgate(A,B)
print("|"+str(A)+"|"+str(B)+"|"+str(res)+"\t|")
A=1
B=0
res=andgate(A,B)
print("|"+str(A)+"|"+str(B)+"|"+str(res)+"\t|")
A=0
B=1
res=andgate(A,B)
print("|"+str(A)+"|"+str(B)+"|"+str(res)+"\t|")
A=0
B=0
res=andgate(A,B)
print("|"+str(A)+"|"+str(B)+"|"+str(res)+"\t|")