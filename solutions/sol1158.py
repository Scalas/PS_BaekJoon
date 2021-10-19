import sys

input = sys.stdin.readline


# 1158 요세푸스 문제
# 원형 수열 [1, 2, ... , n] 에서 k 번째 숫자를 계속해서 제거해나갈 때
# 지워진 순서대로 숫자들을 나열한 리스트를 구하는 문제
def sol1158():
    n, k = map(int, input().split())
    seq = list(range(1, n+1))

    # k가 1이라면 수열을 그대로 출력
    if k == 1:
        return '<%s>' % (', '.join(map(str, seq)))

    answer = []
    idx = 0
    while seq:
        # 다음 삭제위치
        idx = (idx + k - 1) % n

        # 삭제
        answer.append(seq.pop(idx))
        n -= 1

    return '<%s>' % (', '.join(map(str, answer)))
