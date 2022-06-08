import sys

input = sys.stdin.readline


# 1111 IQ Test
# n개의 숫자가 주어지고 숫자간의 관계가 seq[i] * a + b = seq[i+1] 이라고 할 때
# 규칙에 따라 다음 숫자를 구하는 문제
# 단, 다음 수가 여러개일 수 있다면 A를, 다음 수를 구할 수 없다면 B를 반환해야한다.
def sol1111():
    n = int(input())
    seq = list(map(int, input().split()))

    # 하나의 숫자만 주어질 경우 다음 수로 가능한 것은 무수히 많음
    if n == 1:
        return 'A'

    # 두개의 숫자만 주어질 경우
    if n == 2:
        # 두 숫자가 같다면 다음 수도 같음을 알 수 있음
        if seq[0] == seq[1]:
            return seq[0]

        # 두 숫자가 다르다면 다음 수로 가능한 것은 무수히 많음
        else:
            return 'A'

    # 첫 세개의 수를 사용하여 연립방정식으로 a와 b를 특정
    # S3 - S2 = (S2 - S1) * a
    u = seq[1] - seq[0]
    v = seq[2] - seq[1]

    # 첫 두 수가 같은 경우
    # 나머지 수도 모두 같은지 확인하여 같다면 그 수를 그대로 반환
    # 같지 않다면 B 반환
    if not u:
        for i in range(2, n):
            if seq[i] != seq[0]:
                return 'B'
        return seq[0]

    # 특정한 a가 정수가 아닐 경우
    if v % u:
        return 'B'

    a = v // u
    b = seq[1] - seq[0] * a

    # 나머지 수들에 대해 식이 성립하는지 확인
    for i in range(3, n):
        # 하나라도 성립하지 않는다면 다음 수를 알아낼 수 없음
        if seq[i-1] * a + b != seq[i]:
            return 'B'

    # 조건식이 맞다는 것을 확인했을 경우 마지막 수에 a를 곱하고 b를 더한 값 반환
    return seq[-1] * a + b
