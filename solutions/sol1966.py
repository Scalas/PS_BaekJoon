import sys

input = sys.stdin.readline


# 1966 프린터 큐
# 우선순위가 가장 높은 문서가 나올 때 까지 이전 문서를 맨 뒤로 보내는 방식으로
# 특정 문서가 몇 번째로 출력되는지 구하는 문제
# 우선순위의 중복이 허용되기 떄문에 정렬로는 해결이 불가능
# 최댓값의 인덱스를 찾아 그 전까지의 문서는 모두 popleft, append 하기를 반복하면 해결 가능하다


# 리스트 연산으로 구현
def sol1966():
    res = []
    # 테스트케이스 루프
    for _ in range(int(input())):
        n, m = map(int, input().split())

        # 문서의 중요도와 초기 인덱스를 묶어서 리스트형태로 저장
        docs = list(zip(map(int, input().split()), range(n)))

        # 프린트 시작
        for i in range(1, n + 1):
            # 가장 우선도가 높은 문서중 가장 앞에 있는 문서를 출력
            # 문서의 초기인덱스가 m과 같다면 res에 답을 append하고 다음 테스트케이스로
            p = max(docs, key=lambda x: x[0])
            if p[1] == m:
                res.append(i)
                break

            # 실제로는 출력할 문서가 나올때까지 모든 문서를 하나하나 큐의 맨 뒤로 보내야하지만
            # 빠르고 간결하게 처리하기 위해 리스트 슬라이싱을 사용하여 같은 결과를 낸다.
            # 출력할 문서를 기준으로 좌우를 슬라이싱한뒤 순서를 바꾸어 이어붙인다.
            pi = docs.index(p)
            docs = docs[pi + 1:] + docs[:pi]

    return '\n'.join(map(str, res))
