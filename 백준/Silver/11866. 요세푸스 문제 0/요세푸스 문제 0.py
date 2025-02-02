N, K = map(int, input().split())

next = [i+1 for i in range(N+1)]
next[N] = 1
#print(next)

cur = 0
result = []
rm_cnt = 0
while rm_cnt < N:
    for _ in range(K-1):
        cur = next[cur]
    result.append(next[cur])
    next[cur] = next[next[cur]]
    rm_cnt += 1
result = list(map(str, result))
print('<' + ", ".join(result) + '>' )    