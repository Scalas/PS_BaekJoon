import sys
from heapq import heappush, heappop, heapify

input = sys.stdin.readline
MOD = 1 << 64


# 2878 캔디캔디
# n명의 친구가 각각 자신이 받고싶은 사탕의 갯수를 문자로 알려주고
# m개의 사탕을 적절히 나누어주는 것으로 각 친구들의 분노의 합을 최소화하는 문제
# 분노의 크기는 받고싶은 사탕의 갯수에 비해 부족하게 받았을 경우 부족한 갯수의 제곱만큼이 된다.
def sol2878():
    m, n = map(int, input().split())
    required = [int(input()) for _ in range(n)]

    # 부족한 갯수가 많아도 max_val을 넘지 않도록 할 때
    # 필요한 사탕의 갯수를 구하는 함수
    def check(max_val):
        cnt = 0
        for num in required:
            if num > max_val:
                cnt += (num - max_val)
        return cnt

    # 가장 쉬운 해결책은 매 순간 가장 많은 사탕이 부족한 친구에게 사탕을 한개씩 주는 것을
    # m번 반복하는 것이지만 이는 m이 매우 크기 때문에 시간초과가 발생
    # 부족한 갯수의 최댓값을 제한하여 최대한 잘라내면 결과적으로 그 최댓값보다 적게 부족한
    # 친구들에게는 더이상 사탕을 나누어줄 필요가 없으며 남은 사탕은 모두 그 최댓값만큼
    # 부족한 친구들에게 하나씩 나누어주는 것이 최선임을 알 수 있음

    # 이분탐색으로 부족한 사탕의 최댓값을 구함 => O( log(2 * 10^9) )
    s, e = 0, max(required)
    max_cnt = 0
    while s < e:
        mid = (s + e) // 2
        cnt = check(mid)
        if cnt <= m:
            max_cnt = max(max_cnt, cnt)
            e = mid
        else:
            s = mid + 1

    # 부족한 사탕의 수의 제곱(분노)을 모두 더함
    # 이 때, 최댓값과 같은 사탕 수는 아직 나눠주지 않은 남은 사탕 수만큼
    # 제곱 전에 1씩 빼서 계산된다
    remain = m - max_cnt
    answer = 0
    for num in required:
        num = min(num, e)
        if num == e and remain:
            answer = (answer + (num - 1) ** 2) % MOD
            remain -= 1
        else:
            answer = (answer + num ** 2) % MOD

    return answer
