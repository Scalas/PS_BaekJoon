import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = 10 ** 9 + 1


# 2461 대표 선수
# n개의 학급에 각각 m명의 학생이 존재할 때
# 각 학급에서 한명씩 대표를 골라 대표들의 실력중 최댓값과 최솟값의 차가 최소가 되게 하려한다
# 가능한 최댓값과 최솟값의 차를 구하는 문제
def sol2461():
    n, m = map(int, input().split())
    max_count = n * (m-1)
    classes = [list(map(int, input().split())) for _ in range(n)]
    for c in classes:
        c.sort()

    q = []
    maxv, minv = 0, INF
    # 각 학급에서 선택된 학생의 능력치 init_std
    # 그 학급에서 다음으로 높은 능력치를 가진 학생의 능력치 nxt_std
    # 다음으로 선택될 학생의 인덱스
    # 학급번호
    # 위의 순서대로 튜플을 생성하여 힙에 삽입
    for i in range(n):
        init_std = classes[i][0]
        nxt_std = classes[i][1] if m > 1 else INF
        heappush(q, (init_std, nxt_std, 1, i))
        maxv = max(maxv, init_std)
        minv = min(minv, init_std)

    cnt = 0
    answer = maxv - minv
    # 모든 학급의 마지막 학생까지 대표선수로 선발해볼 때 까지 반복
    while cnt < max_count:
        # 가장 능력치가 낮은 학생을 선발한 학급의 정보
        # 능력치가 같다면 다음으로 능력치가 높은 학생의 능력치가 가장 낮은 학급
        cur, nxt, j, i = heappop(q)

        # 현재 최댓값-최솟값 으로 answer 갱신
        answer = min(answer, maxv - cur)

        # 만약 가장 능력치가 낮고 그중에서도 다음 학생의 능력치도 가장 낮은 학급에
        # 다음으로 선발할 학생이 없다면(nxt == INF) 더이상 능력차를 줄일 방법은 없음
        if nxt == INF:
            break

        # 다음 학생을 선택한 상태로 학급정보를 수정하고 큐에 삽입
        # 최댓값 추적을 위해 maxv 갱신
        ncur = nxt
        nnxt = classes[i][j] if m > j else INF
        nj = j + 1
        heappush(q, (ncur, nnxt, nj, i))
        maxv = max(maxv, ncur)

    return answer


if __name__ == '__main__':
    print(sol2461())
