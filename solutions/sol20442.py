import sys

input = sys.stdin.readline


# 20442 ㅋㅋ루ㅋㅋ
# R만 존재하는 문자열은 ㅋㅋ루ㅋㅋ 문자열
# ㅋㅋ루ㅋㅋ문자열 양쪽에 K가 붙어있는 문자열은 ㅋㅋ루ㅋㅋ 문자열
# K와 R로만 이루어진 문자열이 주어졌을 때 주어진 문자열의 부분 문자열중
# 가장 긴 ㅋㅋ루ㅋㅋ문자열의 길이를 구한는 문제
def sol20442():
    string = input().rstrip()
    n = len(string)

    # R의 갯수 누적합
    rc = [0] * (n + 1)
    for i in range(n):
        rc[i] = rc[i-1] + (1 if string[i] == 'R' else 0)

    s, e = 0, n - 1
    # 가장 긴 ㅋㅋ루ㅋㅋ 문자열의 길이는 문자열 전체 문자열의 R의 갯수 이상
    answer = rc[n - 1]

    # 양쪽에 붙은 k 갯수
    kc = 0
    while s < e:
        # 양끝에 R이 존재한다면 패스
        if string[s] == 'R':
            s += 1
        elif string[e] == 'R':
            e -= 1

        # 양 끝이 모두 k일 경우
        # 구간내의 R의 갯수 + kc 로 answer 값 갱신
        else:
            kc += 2
            s += 1
            e -= 1
            mid = rc[e] - rc[s - 1]
            if mid:
                answer = max(answer, mid + kc)

    return answer
