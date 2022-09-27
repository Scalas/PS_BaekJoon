import sys

input = sys.stdin.readline


# 14713 앵무새
# n 마리의 앵무새에게 띄어쓰기로 구분된 여러개의 단어로 구성된 문장 하나씩을 기억하게하고
# 각 앵무새는 상대에게 문장을 순서대로 말하되, 단어 단위로 끊어말하며 단어 하나를 말할 때 마다
# 다른 앵무새가 말을 끊고 자신의 말을 하는 경우가 있다고 한다.
# 각 앵무새가 들은 문장과 앵무새들이 하는 말을 받아적은 문장이 주어졌을 때
# 처음에 주어진 문장들로부터 나올 수 있는 결과를 제대로 받아적은 것인지 확인하는 문제
def sol14713():
    n = int(input())

    # 각 앵무새가 기억한 단어들의 리스트(순서대로)와 단어의 총 갯수
    s = []
    total = 0
    for _ in range(n):
        words = input().split()
        total += len(words)
        s.append(words)

    # 받아적은 단어들의 리스트와 총 갯수
    l = input().split()

    # 단어 갯수가 다르다면 잘못 받아적음
    if len(l) != total:
        return 'Impossible'

    # 각 문장의 몇 번째 단어를 볼 차례인지 나타내는 인덱스
    indexes = [0] * n

    # 받아적은 단어를 순서대로 어느 앵무새가 말한 문장에서 찾아야하는지 확인
    for word in l:
        check = False
        for i in range(n):
            if indexes[i] == len(s[i]):
                continue
            if s[i][indexes[i]] == word:
                indexes[i] += 1
                check = True
                break

        # 만약 어느 앵무새의 문장에서도 찾을 수 없다면 잘못 받아적은 것
        if not check:
            return 'Impossible'

    return 'Possible'
