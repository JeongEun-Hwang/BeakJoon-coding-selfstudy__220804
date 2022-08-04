#A+B-7
# T :테스트 케이스 개수

import sys

T = int(sys.stdin.readline())
# A,B<10

for i in range(1,T+1):
    A,B = map(int, sys.stdin.readline().split())
    print("Case #{} : {}".format(i, A+B))


