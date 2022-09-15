import sys

input = sys.stdin.readline


# 13164 행복 유치원
# n명의 학생의 키가 오름차순으로 주어지고 이 학생들을 최소 1명의 학생으로 구성된 팀 k개로 나누려고 한다.
# 각 팀의 팀 티셔츠를 제작하는 비용은 팀에서 키가 가장 큰 아이와 가장 작은 아이의 키차이만큼 들어간다고 할 떄
# k개의 팀을 나눴을 때 팀 티셔츠 제작 비용의 합의 최솟값을 구하는 문제
def sol13164():
    n, k = map(int, input().split())

    # 중복을 제거한 키의 목록을 구함
    seq = []
    for num in map(int, input().split()):
        if seq and seq[-1] == num:
            continue
        seq.append(num)

    # 키가 중복되는 학생 수
    dup = n - len(seq)

    # n명의 학생을 k개의 팀으로 만들기 위해 필요한 병합 수
    merge_count = n - k

    # 중복을 제거한 후의 키의 갯수
    n = len(seq)

    # 같은 키의 학생들을 팀으로 묶는 것 만으로 k 개의 팀을 만들 수 있는 경우
    # 비용의 합은 0이 됨
    if dup >= merge_count:
        return 0

    # 같은 키의 학생들을 먼저 팀으로 묶음
    merge_count -= dup

    # 각 키값간의 차이를 오름차순 정렬한 뒤 작은 것부터 merge_count 개 만큼 더한 값이
    # 티셔츠 제작 비용의 최솟값이 된다.
    diff = []
    for i in range(n - 1):
        diff.append(seq[i + 1] - seq[i])

    return sum(sorted(diff)[:merge_count])
