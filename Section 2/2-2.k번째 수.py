import sys

sys.stdin = open("../../섹션 2/2. K번째 수/in1.txt", "rt")
T = int(input())

for i in range(T):
    n, s, e, k = map(int, input().split())
    given_list = list(map(int, input().split()))

    extract_list = given_list[s-1:e]
    extract_list.sort()
    print("#%d %d" %(i+1, extract_list[k-1]))
