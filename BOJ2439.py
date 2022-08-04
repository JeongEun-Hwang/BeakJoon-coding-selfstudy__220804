# 별찍기 오른쪽 정렬

N = int(input())

for i in range(N):
    print((' '* (N-i-1))+('*'*(i+1)))