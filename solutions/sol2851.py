import sys

input = sys.stdin.read


# 2851 슈퍼 마리오
# sum(seq[0:k]) 가 100에 가장 가까울 때의 값을 구하는 문제 (차이가 똑같다면 큰 값을 선택)
def sol2851():
    mushroom = [*map(int, input().split())]
    answer = 0
    for num in mushroom:
        tmp_answer = answer + num
        if tmp_answer >= 100:
            answer = answer if 100-answer < tmp_answer - 100 else tmp_answer
            break
        answer = tmp_answer
    return answer
