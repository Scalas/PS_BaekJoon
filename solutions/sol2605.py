import sys

input = sys.stdin.read


# 2605 줄 세우기
# 1 ~ n 까지의 학생이 뽑은 번호표에 따라 순서를 변경하여 출력하는 문제
def sol2605():
    n, *sel = map(int, input().split())
    answer = [1]
    for i in range(1, n):
        answer.append(i+1)
        for _ in range(sel[i]):
            answer[i], answer[i-1] = answer[i-1], answer[i]
            i -= 1
    return ' '.join(map(str, answer))
