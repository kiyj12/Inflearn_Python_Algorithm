import sys

sys.stdin = open("../../섹션 2/3. k번째 큰 수/in5.txt", "rt")

n, k = map(int, input().split())
g_list = list(map(int, input().split()))

sum_list = []
for f in range(len(g_list)):
    first = g_list[f]
    for s in range(f+1, len(g_list) - 1):
        second = g_list[s]
        for t in range(s+1, len(g_list)):
            third = g_list[t]
            sum_list.append(first + second + third)

sum_list = list(set(sum_list))
sum_list.sort(reverse=True)
print(sum_list[k-1])

