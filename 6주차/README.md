# 2026-10-08

-얕은 복사
ex)
temps = [28, 31, 33, 35, 27, 26, 25]
values = temps #얕은 복
print(temps) # temps 리스트 출력
values[3] = 39 # values 리스트 변경
print(temps) # temps 리스트가 변경되었다. 

-깊은 복사
ex)
temps = [28, 31, 33, 35, 27, 26, 25]
values = list(temps) #깊은 복사
