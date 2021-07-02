import sys
from collections import Counter

input = sys.stdin.readline


# 2805 나무자르기
# 통나무를 같은 높이에 매달린 벌목기로 잘라 윗부분만을 가져갈 때
# 가져가는 나무의 길이의 합이 m이상이 되도록 하는 벌목기 높이의 최댓값을 구하는 문제
# 이분탐색을 사용하여 풀 수 있다

# 높이의 범위를 1부터 가장 긴 통나무의 길이-1로 잡았을 때
# 높이가 mid 일때 가져가는 통나무의 길이의 합을 단순히 반복문을 두번 돌려 구했을 때
# 시간초과는 발생하지 않지만 상당한 시간이 소요
def sol2805():
    n, m = map(int, input().split())
    woods = list(map(int, input().split()))
    s, e = 1, max(woods)-1
    answer = 0
    while (s <= e):
        mid = (s + e) // 2
        if (sum([wood - mid for wood in woods if wood > mid]) >= m):
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
    print(answer)


# 길이가 같은 통나무가 여러개 있을 수 있기 때문에 Counter 클래스를 사용
# 가져갈 통나무의 길이의 합을 (나무의길이-벌목기높이)*나무의갯수 로 구함
def sol2805_2():
    n, m = map(int, sys.stdin.readline().split())
    woods = Counter(map(int, sys.stdin.read().split())).items()
    s, e = 0, max(woods)[0]
    answer = 0
    while s <= e:
        mid = (s + e) // 2
        if sum([(wood - mid) * c if wood > mid else 0 for wood, c in woods]) >= m:
            answer = mid
            s = mid + 1
        else:
            e = mid - 1
    print(answer)
