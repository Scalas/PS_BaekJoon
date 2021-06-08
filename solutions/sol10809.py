import sys

input = sys.stdin.readline


# 10809 알파벳 찾기
# 각 알파벳이 입력받은 단어에서 처음 등장하느 위치를 출력하는 문제
def sol10809():
    count = ['-1'] * 26
    for i, c, in enumerate(input().rstrip()):
        idx = ord(c) - ord('a')
        if count[idx] == '-1':
            count[idx] = str(i)
    print(' '.join(count))
