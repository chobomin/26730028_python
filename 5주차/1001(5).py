#여러 개의 정수를 한 줄에 입력받아 가장 큰 값을 출력하는 프로그램
a=list(map(int,input().split()))

print(max(a))
"""
for i in range(1, len(a)):
    if max_value <a[i]:
        max_value=a[i]

print(max_value)
"""
