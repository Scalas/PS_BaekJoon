import sys

input = sys.stdin.read


# 1495 기타리스트
# 곡의갯수 n과 시작볼륨 s, 볼륨 상한값 m 이 주어지고 각 곡의 볼륨 조정값 리스트 v 가 주어졌을 때
# 곡 i를 연주하기 전에 이전 볼륨에서 v[i] 를 더하거나 빼는 것으로 볼륨을 조정하고 공연을 해야한다.
# 마지막 곡을 연주할 때 가능한 최대 볼륨을 구하되, 곡의 볼륨은 0 이상 m 이하여야 하며 마지막 곡을
# 연주할 수 없는 경우 -1을 반환해야 한다.
def sol1495():
    # 곡의 갯수, 시작볼륨, 볼륨 상한값, 조정값 리스트
    n, s, m, *volumes = map(int, input().split())

    # 현재 곡을 연주하는데 사용 가능한 볼륨값 집합
    cand = {s}

    # 각 곡의 조정값을 이전 곡에서 사용 가능했던 볼륨값들에 더하거나 빼는 것으로
    # 이번 곡에서 사용 가능한 볼륨값 집합을 생성한다.
    for v in volumes:
        u = set()
        for c in cand:
            add, sub = c + v, c - v
            if 0 <= add <= m:
                u.add(add)
            if 0 <= sub <= m:
                u.add(sub)
        cand = u

    # 마지막 곡에서 사용 가능한 볼륨값의 집합중 최댓값을 반환한다.
    # 만약 마지막 곡에서 사용 가능한 볼륨값이 존재하지 않는다면 -1을 반환한다.
    return max(cand) if cand else -1
