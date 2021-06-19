from sys import stdin


# 2108 통계학
# 입력받은 수의 산술평균, 중간값, 최빈값, 범위를 구하는 문제
# 카운팅 정렬을 활용하여 해결 가능하다
def sol2108():
    n = int(stdin.readline())

    # 입력받은 수를 카운팅
    counts = [0]*8001
    for i in stdin:
        num = int(i)
        counts[num+4000] += 1

    maxc = max(counts)  # 최빈값의 등장 횟수
    mode = mcnt = 0
    idx = 0
    med = None
    mi, ma = 4001, -4001
    for i in range(8001):
        # 등장하지 않은 숫자일 경우 continue
        cnt = counts[i]
        if cnt == 0:
            continue

        num = i-4000

        # 숫자의 총합
        s += num*counts[i]

        # 두 번째 최빈값이 등장할때까지 최빈값 갱신
        if cnt == maxc and mcnt < 2:
            mode = num
            mcnt += 1

        # 최소, 최대값 갱신
        mi = min(mi, num)
        ma = max(ma, num)

        # 중앙값의 위치를 넘어간 순간 그 수를 중앙값으로 대입
        idx += counts[i]
        if idx >= n//2+1 and med == None:
            med = num

    print(round(s/n), med, mode, ma-mi, sep='\n')
