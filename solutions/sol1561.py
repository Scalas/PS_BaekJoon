import sys

input = sys.stdin.readline


# 1561 놀이 공원
# n명의 아이가 차례대로 m개의 1인승 놀이기구에 탑승하려한다.
# m개의 놀이기구는 각각 분단위의 운행시간을 가지며(최대30분)
# 운행시간이 끝나야 다음 손님을 태울 수 있다.
# 이 때, n번쨰 아이가 타게될 놀이기구는 몇번 놀이기구인지 구하는 문제
def sol1561():
    n, m = map(int, input().split())
    # 아이의 수가 놀이기구 수보다 작을 경우 바로 모두가 탈 수 있기 때문에
    # n번째 놀이기구가 마지막 아이가 탈 놀이기구가 됨
    if n <= m:
        return n

    # 놀이기구가 하나뿐이라면 1번 놀이기구가 마지막 아이가 탈 놀이기구가 됨
    if m == 1:
        return 1

    # 놀이기구가 한번 운행하는데 걸리는 시간
    time = list(map(int, input().split()))



    # 처음으로 n명 이상의 아이를 태울 수 있게되는 시간을 이분탐색으로 구함
    s, e = 1, max(time) * (n//m)

    # 처음에 탄 m명의 아이 제외
    n -= m

    while s < e:
        mid = (s + e) // 2
        max_child = sum(map(lambda x: mid//x, time))
        if max_child < n:
            s = mid+1
        else:
            e = mid

    # 1분 전까지 태울 수 있었던 아이의 수를 제외
    n -= sum(map(lambda x: (e-1)//x, time))

    # e분째에 새로운 아이를 태울 수 있는 놀이기구는 운행시간이 e의 약수인 것 뿐
    # e의 약수이면서 남은 n번쨰 놀이기구를 탐색
    cnt = 0
    for i in range(m):
        if not e % time[i]:
            cnt += 1
            if cnt == n:
                return i+1
