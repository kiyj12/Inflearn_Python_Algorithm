import sys

sys.stdin = open("../../섹션 2/1. k번째 약수/in1.txt", "rt")

n, k = map(int, input().split())

i = 1
divisor_list = []

while i <= n:
    if n % i == 0:
        divisor_list.append(i)
    i += 1

if len(divisor_list) < k:
    print(-1)
else:
    print(divisor_list[k-1])