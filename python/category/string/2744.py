N=list(input())
s=""
for i in N:
    idx=N.index(i)
    if i.islower():
        N[idx]=i.upper()
    else:
        N[idx]=i.lower()
    s+=N[idx]
print(s)