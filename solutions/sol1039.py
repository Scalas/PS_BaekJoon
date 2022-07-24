import sys
from math import floor, log10

input = sys.stdin.readline


# 1039 교환
# 100만 이하의 정수 n과 연산횟수 k가 주어졌을 때
# 서로 다른 자릿수 두개의 자리를 맞바꾸는 연산을 k번 하여
# 얻을 수 있는 최대 정수값을 구하는 문제
def sol1039():
    n, k = map(int, input().split())
    # 정수 n의 자릿수
    m = floor(log10(n)) + 1

    # 정수의 i, j 번째 자릿수를 뒤바꾸는 함수 (0번째가 1의자리)
    # 만약 바꾼 결과 맨 앞자리에 0이가게되는 경우 -1을 반환
    def swap(num, i, j):
        idigit = 10 ** i
        inum = (num // idigit) % 10
        jdigit = 10 ** j
        jnum = (num // jdigit) % 10
        if j == m - 1 and inum == 0:
            return -1
        return num - (idigit * inum + jdigit * jnum) + (idigit * jnum + jdigit * inum)

    # 연산을 0번 했을 때 만들 수 있는 정수는 n 하나뿐 
    q = {n}
    cnt = -1
    while q:
        cnt += 1
        # 연산 k회 완료시 종료
        if cnt == k:
            break
        nq = set()
        for cur in q:
            # 가능한 i, j 쌍에 대해 자리바꿈 시도
            for i in range(m - 1):
                for j in range(i + 1, m):
                    num = swap(cur, i, j)
                    # 바꾼 결과 0으로 시작하게되는 경우는 제외
                    if num < 0:
                        continue
                    nq.add(num)
        q = nq
        
    # k회의 연산에 성공한 경우 얻을 수 있는 정수중 최댓값 반환
    # 실패한 경우 -1 반환
    return max(q) if cnt == k else -1
