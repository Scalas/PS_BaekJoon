import sys
from bisect import bisect_left

input = sys.stdin.readline


# 20191 줄임말
# 문자열 t를 n번 이어붙인 문자열에서 순서를 바꾸지 않고 일부 문자를 제거하여 문자열을 s로 만들 때
# 문자열 s를 만들 수 있다면 n의 최솟값을 구하는 문제
# 단, s를 만들 수 없다면 -1을 반환
def sol20191():
    s = input().rstrip()
    t = input().rstrip()
    n = len(t)

    # 문자열 t에서의 각 알파벳의 인덱스 리스트(오름차순)
    index = dict()
    for c in range(ord('a'), ord('z') + 1):
        index[chr(c)] = []
    for i in range(n):
        index[t[i]].append(i)

    # 시작 idx는 -1
    idx = -1

    # 문자열 t의 반복 횟수는 1
    loop = 1

    # 문자열 s의 문자 순회
    for c in s:
        # 문자열 t에서 문자 c가 등장하는 인덱스 리스트
        index_list = index[c]

        # 리스트가 비어있다면 만들 수 없는 문자열이므로 -1 반환
        if not index_list:
            return -1

        # 리스트 내의 인덱스가 현재 인덱스와 같거나 그보다 이전일 경우 문자열 t를 한번 더 이어붙여야함
        # loop 수를 늘리고 현재 인덱스를 리스트 내의 인덱스중 최솟값으로 이동
        if index_list[-1] <= idx:
            loop += 1
            idx = index_list[0]

        # 그렇지 않을 경우 이분탐색으로 리스트 내의 인덱스 중 현재 인덱스보다 크면서 가장 작은 인덱스로 이동
        else:
            idx = index_list[bisect_left(index_list, idx + 1)]

    # 순회가 끝난 후 반복 횟수를 반환
    return loop
