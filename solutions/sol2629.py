import sys

input = sys.stdin.readline


# 2629 양팔저울
# 양팔저울과 무게추를 사용하여 구슬의 무게를 확인 가능한지 구하는 문제
# 냅색 문제의 응용으로 추가 하나 추가될 때 마다 확인 가능한 무게를 추가해나가면 해결 가능하다
# 다만 냅색과 조금 다른점은 냅색은 무게를 추가해나가기만 하면 해결됐지만
# 양팔저울은 반대편에도 추를 놓을 수 있기 때문에
# 무게를 뺀 값의 절댓값도 추가해줄 필요가 있다
def sol2629():
    n = int(input())
    weights = list(map(int, input().split()))

    dp = {0}
    for weight in weights:
        u = set()
        for w in dp:
            u.add(w + weight)
            u.add(abs(w - weight))
        dp |= u

    m = int(input())
    answer = []
    for marble in map(int, input().split()):
        answer.append('Y' if marble in dp else 'N')

    print(' '.join(answer))
