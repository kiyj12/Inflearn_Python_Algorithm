import sys

sys.stdin = open("../../섹션 2/3. k번째 큰 수/in5.txt", "rt")

n, k = map(int, input().split())
g_list = list(map(int, input().split()))

# 애초에 답을 담을 리스트 자체를 set으로 해서 중복되지 않은 숫자만 넣도록 했다.
res = set()
for f in range(len(g_list)):
    for s in range(f+1, len(g_list) - 1):
        for t in range(s+1, len(g_list)):
            set.add(g_list[f]+g_list[s]+g_list[t])

res = list(res)
res.sort(reverse=True)
print(res[k-1])

