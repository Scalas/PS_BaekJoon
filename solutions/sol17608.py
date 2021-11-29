import sys

input = sys.stdin.read


# 17608 막대기
# 높이가 다른 막대를 일렬로 세웠을 때
# 오른쪽에서 보이는 막대의 수를 구하는 문제
def sol17608():
    n, *bars = map(int, input().split())
    answer = 0
    eye = 0
    for bar in bars[::-1]:
        if eye < bar:
            eye = bar
            answer += 1
    return answer
