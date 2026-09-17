#방법1
for a in range(5,0,-1):
    for b in range(a):
        print("*",end="")
    print()

"""
#방법2
x=5
for i in range(1,6):
    print(" "*x+"*"*i)
    x-=1

#방법3
for i in range(1,6):
    print(" "*(5-i)+"*"*i)

"""
