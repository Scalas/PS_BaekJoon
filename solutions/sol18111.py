import sys

input = sys.stdin.read
n, m, b, *ground = map(int, input().split())


# 18111 마인크래프트
# 가진 블록의 수와 n * m 크기의 땅의 높이가 주어졌을 때
# 2초를 소모하여 땅을 한칸 깎고 블록을 하나 얻거나
# 1초를 소모하여 블록을 하나사용하고 땅의 높이를 증가시키는 행위를 반복하여
# 땅을 고르기 위해 소모되는 최소 시간과 그 때의 땅의 높이를 구하는 문제
# 같은 시간이라면 보다 땅의 높이가 높은 경우를 구한다.
def sol18111():
    # 현재 땅의 최소, 최대높이
    minh, maxh = min(ground), max(ground)

    # 최대높이와의 차의 합
    t_max = 0

    # smt[i] 는 높이가 i 이하인 땅의 갯수
    smt = [0] * (maxh+1)
    for gh in ground:
        smt[gh] += 1
        t_max += (maxh - gh)

    for i in range(maxh):
        smt[i+1] += smt[i]

    # 시간과 높이를 최대치로 초기화
    time = 10 ** 9
    height = 257

    # 블록을 쌓기만하여 최대높이에 맞췄을 경우의 시간과 높이, 블록의 갯수
    t = t_max
    h = maxh
    block = b - t

    # 블록의 갯수가 음수라면 실현 불가능한 상황이기 때문에 반영하지 않음
    if block >= 0:
        time, height = t, h

    # 평준화 높이를 낮춰가며 검사
    for h in range(maxh-1, minh-1, -1):
        # 원래 평준화 높이보다 낮았던 블록의 갯수
        lower = smt[h]

        # 원래 평준화 높이보다 높았던 블록의 갯수
        higher = smt[-1] - smt[h]

        # 높았던 블록은 1씩 깎아야하기 때문에 2초씩 시간이 추가
        # 낮았던 블록은 1씩 덜 쌓아도 되기 때문에 1초씩 시간이 감소
        t += (higher * 2 - lower)

        # 높았던 블록을 깎아서 얻은 블록과 낮았던 블록을 덜 쌓아서 아낀 블록의 수를 더한다
        block += (higher + lower)

        # 블록의 갯수가 0 이상(실현가능)이고 더 빠르게 작업이 끝났다면 최소시간, 높이 갱신
        if block >= 0 and t < time:
            time, height = t, h

    # 시간과 높이 반환
    return ' '.join(map(str, [time, height]))
