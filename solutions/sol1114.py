import sys

input = sys.stdin.readline


# 1114 통나무 자르기
# 길이 l의 통나무와 통나무를 자를 수 있는 위치 k개가 주어지고
# 최대 c번 통나무를 자를 수 있을 때
# 통나무를 자른 결과 가장 긴 통나무조각의 길이의 최솟값과
# 그 때의 자른 위치중 최솟값을 구하는 문제
def sol1114():
    l, k, c = map(int, input().split())
    cut = sorted(map(int, input().split()))[::-1]
    cut.append(0)

    def check(ml):
        cnt = c
        start, pre = l, l
        # 뒤에서부터 자르기
        for cur in cut:
            # 나눌 수 없는 조각의 길이가 ml보다 크다면 불가능
            if pre - cur > ml:
                return 0

            # 조각의 크기가 ml보다 커질 경우
            if start - cur > ml:
                # 자를 수 있다면 자름
                if cnt:
                    cnt -= 1
                    start, pre = pre, cur

                # 자를 수 없다면 불가능
                else:
                    return 0

            # 조각의 크기가 ml이하라면 자르지않고 넘어감 
            else:
                pre = cur

        # 만약 모두 쪼개고도 자르는 횟수가 남아있다면 자를 수 있는 위치중 최솟값 반환
        if cnt:
            return cut[-2]

        # 그 외의 경우 마지막으로 자른 위치 반환
        return start

    # 통나무의 최대길이의 최솟값으로 가능한 값을 탐색
    first = cut[-1]
    s, e = 1, l
    while s < e:
        mid = (s + e) // 2
        res = check(mid)
        if res:
            e = mid
            first = res
        else:
            s = mid + 1

    return ' '.join(map(str, [e, first]))
