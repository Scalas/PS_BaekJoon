import sys

input = sys.stdin.read


# 3687 성냥개비
# 성냥개비로 다음과 같이 숫자를 표현할 수 있을 때
# 2개 : 1
# 3개 : 7
# 4개 : 4
# 5개 : 2, 3, 5
# 6개 : 0, 6, 9
# 7개 : 8
# n개의 성냥개비로 만들 수 있는 수의 최소값과 최대값을 구하는 문제
def sol3687():
    _, *seq = map(int, input().split())

    # 테스트케이스중 최대값
    n = max(seq)

    # dp[i] 는 i개의 성냥개비로 만들수있는 수의 최소, 최댓값
    dp = [
        ['0', '0'],
        ['0', '0'],
        ['1', '1'],
        ['7', '7'],
        ['4', '11'],
        ['2', '71'],
        ['6', '111'],
        ['8', '711'],
    ]

    # dp[i][0] 은 dp[i-j][0]에 j개의 성냥개비로 한자리 수를 더해서 만들 수 있는 수의 최소값
    # dp[i][1] 은 dp[i-j][1]에 j개의 성냥개비로 한자리 수를 더해서 만들 수 있는 수의 최대값
    for i in range(8, n+1):
        # 성냥개비 2개를 더하여 만든 최소, 최대값
        min_val = add_num(dp[-2][0], 2, 0)
        max_val = add_num(dp[-2][1], 2, 1)

        for j in range(3, 8):
            # 1개 이하의 성냥개비로는 수를 표현할 수 없음
            if i-j < 2:
                continue

            # j개의 성냥개비를 더해서 만들 수 있는 최소, 최대값으로 min_val, max_val 갱신
            minv = add_num(dp[-j][0], j, 0)
            maxv = add_num(dp[-j][1], j, 1)
            if int(minv) < int(min_val):
                min_val = minv
            if int(maxv) > int(max_val):
                max_val = maxv

        # dp[i] 추가
        dp.append([min_val, max_val])

    return '\n'.join([' '.join(dp[num]) for num in seq])


# 이전 숫자 pre 에 match 개의 성냥을 더하여 만들 수 있는 수 중에
# m이 1이라면 최댓값, 0이라면 최솟값을 반환
def add_num(pre, match, m):
    num = '0'

    # 성냥을 6개 추가 -> 0, 6, 9
    if match == 6:
        if m:
            num = '9'
        else:
            # 최솟값의 맨 앞자리가 6보다 크다면 6을 맨앞에 붙여야 최솟값을 만들 수 있음
            # 최솟값의 맨 앞자리가 6보다 작다면 0을 앞에서 두번째 자리에 붙여야 최솟값을 만들 수 있음
            num = '6' if pre[0] > '6' else '0'

    # 성냥을 5개 추가 -> 2, 5
    elif match == 5:
        if m:
            num = '5'
        else:
            num = '2'

    # 성냥을 2개 추가 -> 1
    elif match == 2:
        num = '1'

    # 성냥을 3개 추가 -> 7
    elif match == 3:
        num = '7'

    # 성냥을 4개 추가 -> 4
    elif match == 4:
        num = '4'

    # 성냥을 7개 추가 -> 8
    elif match == 7:
        num = '8'

    # 최댓값을 구하는 경우
    if m:
        # 최댓값은 자릿수가 내림차순인 상태
        # 추가될 한자리수가 내림차순을 유지하며 삽입될 자리를 찾아 삽입한 결과를 반환
        maxi = 0
        while maxi < len(pre) and pre[maxi] > num:
            maxi += 1
        return pre[:maxi] + num + pre[maxi:]

    # 최솟값을 구하는 경우
    else:
        # 추가될 한자리수가 0일경우 맨 앞에서 두번째 자리에 삽입한 결과를 반환
        if num == '0':
            return pre[0]+num+pre[1:]

        # 0이 아닐경우 0을 제외하고 오름차순을 유지하며 삽입될 자리를 찾아 삽입한 결과를 반환
        else:
            mini = 0
            while mini < len(pre) and pre[mini] < num:
                mini += 1
            return pre[:mini] + num + pre[mini:]
