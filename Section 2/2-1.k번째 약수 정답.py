import sys

sys.stdin = open("../../섹션 2/1. k번째 약수/in2.txt", "rt")

n, k = map(int, input().split())

cnt = 0
for i in range(1, n+1):
    if n % i == 0:
       cnt += 1
    if cnt == k:
        print(i)
        break
        # 원하는 위치의 값을 구하고 나면 정답 리스트를 완성할 필요 없이 끝내도록 했다.
else:
    print(-1)