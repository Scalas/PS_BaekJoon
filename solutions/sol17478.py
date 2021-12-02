import sys

input = sys.stdin.readline
n = int(input())


# 17478 재귀함수가 뭔가요?
# 입력받은 재귀 깊이에 따라 문장을 출력하는 문제
def sol17478():
    answer = []
    answer.append('어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.')
    recursion(answer, 0)
    return '\n'.join(answer)


def recursion(answer, depth):
    if depth == n:
        answer.append('____' * depth + '"재귀함수가 뭔가요?"')
        answer.append('____' * depth + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        answer.append('____' * depth + '"재귀함수가 뭔가요?"')
        answer.append('____' * depth + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        answer.append('____' * depth + '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.')
        answer.append('____' * depth + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        recursion(answer, depth+1)

    answer.append('____' * depth + '라고 답변하였지.')
