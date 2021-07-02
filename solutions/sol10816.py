import sys
from collections import Counter

input = sys.stdin.readline


# 10816 숫자 카드 2
# 단순히 특정 수의 포함여부만이 아니라 몇 개가 들어있는지까지 확인해야하는 문제

# dictionary 를 활용한 카운팅으로 해결한 풀이
# 무난한 실행시간으로 해결
def sol10816():
    input()
    cards = {}
    for num in input().split():
        try:
            cards[num] += 1
        except:
            cards[num] = 1

    input()
    answer = []
    for num in input().split():
        res = cards.get(num)
        answer.append('0' if not res else str(res))

    sys.stdout.write(' '.join(answer))


# 문제의 분류가 이분탐색인만큼 이분탐색을 사용한 접근
# 찾으려는 숫자중 가장 왼쪽에 있는 것과 가장 오른쪽에 있는 것의 인덱스를 각각 탐색(O(logN) * 2)
# 두 인덱스의 차 + 1 이 답이된다
# Python 3으로는 시간초과 발생.  PyPy3으로는 해결이 됨
def sol10816_2():
    input()
    cards = input().split()
    cards.sort()
    answer = []
    input()
    for num in input().split():
        answer.append(search(cards, num))

    print(' '.join(map(str, answer)))


def search(arr, t):
    lres, rres = None, None
    s, e = 0, len(arr) - 1
    while (s <= e):
        m = (s + e) // 2
        if (arr[m] == t and (m == 0 or arr[m - 1] != t)):
            lres = m
            break
        elif (arr[m] < t):
            s = m + 1
        else:
            e = m - 1

    if lres == None:
        return 0

    if (rres == None):
        s, e = 0, len(arr) - 1
        while (s <= e):
            m = (s + e) // 2
            if (arr[m] == t and (m == len(arr) - 1 or arr[m + 1] != t)):
                rres = m
                break
            elif (arr[m] > t):
                e = m - 1
            else:
                s = m + 1

    return rres - lres + 1


# collections 모듈의 Counter 클래스를 사용한 풀이
# list 를 Counter 인스턴스로 변환하면 리스트의 요소를 key, 그 갯수를 value 로 한 dictionary 형태로 저장된다
def sol10816_3():
    input()
    cards = Counter(input().split())
    input()
    answer = []
    for num in input().split():
        res = cards.get(num)
        answer.append('0' if not res else str(res))

    sys.stdout.write(' '.join(answer))
