import sys

input = sys.stdin.readline


# 1969 DNA
# 주어진 DNA들과의 해밍거리의 합이 가장 작은 DNA를 구하는 문제
# 같은 해밍거리의 합을 가진다면 사전순으로 앞선것을 구한다
def sol1969():
    n, m = map(int, input().split())
    dna = [input().rstrip() for _ in range(n)]
    hd = 0
    res = []
    for i in range(m):
        cnt = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
        for j in range(n):
            cnt[dna[j][i]] += 1
        nuc = max(cnt.keys(), key=lambda x:(cnt[x], -ord(x)))
        res.append(nuc)
        hd += sum(cnt.values()) - cnt[nuc]

    return '\n'.join([''.join(res), str(hd)])
