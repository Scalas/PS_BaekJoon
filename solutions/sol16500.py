import sys
import re

input = sys.stdin.read


# 16500 문자열 판별
# 문자열 s와 단어목록이 주어졌을 때
# 단어 목록의 단어들을 이어붙여 문자열 s를 만들 수 있는지 여부를 구하는 문제
# 단어목록의 단어는 여러번 사용 가능하며 이어붙일때 사이에 공백을 넣을 수는 없다
def sol16500():
    s, _, *strings = input().split()
    strings = set(strings)
    n = len(s)

    # dp[i][j] 는 string[i:j+1]가 만들 수 있는 문자열이라면 1, 만들 수 없다면 0
    dp = [[-1] * n for _ in range(n)]

    # 문자열에서 단어 목록의 단어들의 위치를 탐색
    # dp[시작위치][끝위치] 를 1로 초기화
    for string in strings:
        for f in re.finditer(string, s):
            dp[f.start()][f.end()-1] = 1

    def check(l, r):
        if dp[l][r] < 0:
            dp[l][r] = 0
            # 구간의 길이가 2 이상일 경우
            if l < r:
                # 구간을 두 부분으로 나누었을 때 양쪽이 모두 단어로 만들 수 있는 경우를 탐색
                # 양쪽이 모두 단어로 만들 수 있는 경우가 있다면 dp[l][r]을 1로하고 break
                for i in range(l+1, r+1):
                    if check(l, i-1) == 1 and check(i, r) == 1:
                        dp[l][r] = 1
                        break

        return dp[l][r]

    # 문자열 s 전체를 만들 수 있는지 검사하여 결과를 반환
    return check(0, n-1)
