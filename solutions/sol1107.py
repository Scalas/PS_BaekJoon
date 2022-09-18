import sys

input = sys.stdin.readline


# 1107 리모컨
# 숫자 0 ~ 9 와 + - 버튼이 있는 리모컨에서 m개의 숫자 버튼이 고장났을 때
# 채널 100에서 채널 n으로 가기 위해 버튼을 눌러야할 최소 횟수를 구하는 문제
def sol1107():
    n = int(input())
    m = int(input())

    # 고장난 버튼
    broken = [False] * 10
    if m:
        for b in map(int, input().split()):
            broken[b] = True

    # 입력 가능한 채널인지 확인
    def is_available(num):
        if not num:
            return not broken[0]
        while num:
            if broken[num % 10]:
                return False
            num //= 10
        return True

    if n == 100:
        return 0

    # n과의 차가 + - 버튼만을 눌러 이동하는 횟수보다 적은 채널에 대해서 탐색
    # 채널의 자릿수 + n과의 차 의 최솟값을 찾아내 answer를 갱신
    answer = abs(n - 100)
    for diff in range(answer):
        low = n - diff
        if low >= 0 and is_available(low):
            d = 0 if low else 1
            while low:
                d += 1
                low //= 10
            answer = min(answer, diff + d)
            break

        high = n + diff
        if is_available(high):
            d = 0 if high else 1
            while high:
                d += 1
                high //= 10
            answer = min(answer, diff + d)
            break

    return answer
