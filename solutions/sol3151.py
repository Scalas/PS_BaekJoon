import sys

input = sys.stdin.readline


# 3151 합이 0
# n개의 숫자가 주어졌을 때
# 그중 3개를 골라 0이되는 모든 경우의 수를 구하는 문제
# 단, 숫자와 순서가 모두 같아도 뽑힌 숫자의 index가 다르면 다른 경우의 수로 생각한다.
def sol3151():
    n = int(input())
    seq = sorted(map(int, input().split()))
    seq.sort()

    def search_min_bound(start, target):
        s, e = start, n - 1
        if seq[e] < target:
            return -1
        while s < e:
            mid = (s + e) // 2
            if seq[mid] >= target:
                e = mid
            else:
                s = mid + 1
        if seq[e] == target:
            return e
        else:
            return -1

    def search_max_bound(start, target):
        s, e = start, n - 1
        if seq[s] > target:
            return -1
        res = -1
        while s <= e:
            mid = (s + e) // 2
            if seq[mid] <= target:
                res = mid
                s = mid + 1
            else:
                e = mid - 1
        if res == -1:
            return -1
        if seq[res] == target:
            return res
        else:
            return -1

    # 두 수를 고른 뒤 나머지 하나가 될 수 있는 수의 갯수를 두 수중 큰 쪽보다
    # index가 큰 수들 중에서 구하여 모두 더한다.
    answer = 0
    for i in range(n):
        for j in range(i + 1, n - 1):
            need = -(seq[i] + seq[j])
            min_bound = search_min_bound(j + 1, need)
            if min_bound == -1:
                continue
            max_bound = search_max_bound(j + 1, need)
            answer += (max_bound - min_bound + 1)
    return answer
