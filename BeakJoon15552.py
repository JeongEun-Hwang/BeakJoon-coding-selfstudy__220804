#input 대신 sys.stdin.readline을 사용
# 문자열 저장의 경우 r.strip()을 추가
import sys

T = int(sys.stdin.readline())

for i in range(1,T):
    A,B = map(int,sys.stdin.readline().split())
    print(A+B)