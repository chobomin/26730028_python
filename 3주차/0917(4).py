a=[1,2,3]
b=(1,2,3)

def add(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum

print(add(10,20,30,40,50))
