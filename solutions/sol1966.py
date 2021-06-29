import sys

input = sys.stdin.readline


# 1966 프린터 큐
# 우선순위가 가장 높은 문서가 나올 때 까지 이전 문서를 맨 뒤로 보내는 방식으로
# 특정 문서가 몇 번째로 출력되는지 구하는 문제
# 우선순위의 중복이 허용되기 떄문에 정렬로는 해결이 불가능
# 최댓값의 인덱스를 찾아 그 전까지의 문서는 모두 popleft, append 하기를 반복하면 해결 가능하다


# 리스트 연산으로 구현
def sol1966():
    answer = []
    for t in range(int(input())):
        n, m = map(int, input().split())
        docs = [*map(int, input().split())]
        turn = 1
        while True:
            i = docs.index(max(docs))
            if i == m:
                break
            docs = docs[i + 1:] + docs[:i]
            m = m - i - 1 if i < m else len(docs) - i + m
            turn += 1
        answer.append(str(turn))
    print('\n'.join(answer))
