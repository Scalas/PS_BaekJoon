import sys

input = sys.stdin.readline


# 5622 다이얼
# 영어로 표현된 숫자를 다이얼로 누르기 위해 걸리는 시간을 구하는 문제
#
def sol5622():
    dial = {'A': 3, 'B': 3, 'C': 3, 'D': 4, 'E': 4, 'F': 4, 'G': 5, 'H': 5, 'I': 5, 'J': 6, 'K': 6, 'L': 6, 'M': 7,
            'N': 7, 'O': 7, 'P': 8, 'Q': 8, 'R': 8, 'S': 8, 'T': 9, 'U': 9, 'V': 9, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10}
    print(sum([dial[x] for x in input().rstrip()]))
