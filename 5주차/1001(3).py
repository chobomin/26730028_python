#0이 입력될 때까지 정수를 입력받아 리스트에 저장한 후
#짝수번째(두번쨰,네번쨰,여섯번쨰..)값을 공백으로 구분하여 한줄에 출력하는 프로그램
lst=[]

while True:
    n=int(input())
    if n==0:
        break
    lst.append(n)

for i in range(len(lst)):
    if i % 2 ==1:
        print(lst[i], end=" ")
