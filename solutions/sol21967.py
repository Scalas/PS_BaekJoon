import sys

input = sys.stdin.read


# 21967 세워라 반석 위에
# 주어진 수열에서 최댓값과 최솟값의 차가 2를 넘지않는 가장 긴 부분 연속수열의 길이를 구하는 문제


# 첫 번째 시도
# 이분탐색을 활용한 풀이
# 부분수열의 시작과 끝이 모두 왼쪽에있는 경우, 모두 오른쪽에 있는경우, 시작은 왼쪽에 끝은 오른쪽에 있는경우
# 세 가지 경우로 나누어 계산
def sol21967():
    n, *nums = map(int, input().split())
    print(flat(nums))


# 가장 긴 반석 부분수열의 길이를 반환
def flat(nums):
    l = len(nums)

    # 수의 범위가 1~10이기 때문에 부분수열에 포함된 수를 모두 카운팅
    # 양 끝에서 카운트가 0이 아닌 값을 찾아 빠르게 최대, 최소값을 구함
    count = [0 for _ in range(11)]

    mid = l // 2
    if l % 2 == 0:
        left, right = mid-1, mid
        count[nums[left]] += 1
        count[nums[right]] += 1
    else:
        left = right = mid
        count[nums[mid]] += 1

    # 시작이 왼쪽에, 끝이 오른쪽에 있는 경우
    # 중간값에서 시작하여 조건이 만족되는 선에서 최대한 왼쪽으로 확장
    while check(count) <= 2:
        left -= 1
        if left < 0:
            break
        count[nums[left]] += 1
    if left >= 0:
        count[nums[left]] -= 1
    left += 1
    res = right - left + 1

    # 오른쪽으로 최대한 늘리며 조건을 만족하지 못할경우 왼쪽을 한칸 줄이면서 진행
    # 더이상 부분수열의 길이가 늘어나지 않을것으로 판단되면 중지
    tmp = mid - 1 if l % 2 == 0 else mid
    while left <= tmp and (l - left) >= res:
        while check(count) <= 2:
            right += 1
            if right == l:
                break
            count[nums[right]] += 1
        if right < l:
            count[nums[right]] -= 1
        right -= 1
        res = max(res, right-left+1)
        count[nums[left]] -= 1
        left += 1

    # 시작과 끝이 각각 왼쪽, 오른쪽에 있는 부분수열의 길이가 전체 수열의 절반을 넘길 경우
    # 좌, 우를 탐색해도 이보다 긴 수열은 나오지 않기 때문에 그대로 반환
    if res >= mid:
        return res

    # 그렇지 않다면 좌, 우의 부분수열에 대해 재귀호출한 결과와 비교하여 가장 큰 값을 반환
    if l % 2 == 0:
        return max(res, flat(nums[:mid]), flat(nums[mid:]))
    else:
        return max(res, flat(nums[:mid]), flat(nums[mid+1:]))


# 최댓값 - 최솟값을 반환
def check(count):
    mi, ma = 1, 10
    while count[mi] == 0:
        mi += 1
    while count[ma] == 0:
        ma -= 1
    return ma - mi


# 두 번째 시도
# 첫 번째 시도에서는 너무 어렵게 생각했지만 사실은 간단한 문제였다
# 수의 범위가 작다는점에 착안해서 최소값 x가 [1, 8] 일 때
# x이상 x+2 이하인 수가 연속되는 길이중 최댓값을 구하면 해결할 수 있었다
def sol21967_2():
    n, *nums = map(int, input().split())
    answer = 0
    for x in range(1, 8):
        cnt = 0
        for num in nums:
            if x <= num <= x+2:
                cnt += 1
                answer = max(answer, cnt)
            else:
                cnt = 0

    print(answer)


# 세 번째 시도
# 동적 계획법을 활용해서 더 빠르게 풀 수도 있었다
def sol21967_3():
    n, *nums = map(int, input().split())
    dp = [0] * (n + 1)

    mi = ma = 0
    cnt = 0
    i = 0
    # 우선 최소, 최대 값의 인덱스를 갱신해나가며 조건을 만족하는 수열의 길이를 늘려나간다
    while i < n:
        mi = i if nums[i] <= nums[mi] else mi
        ma = i if nums[i] >= nums[ma] else ma

        # 그러던중 조건을 만족하지 않는 시점이 오면 원인이 되는 최솟값, 최댓값 중 인덱스가 앞에 있는쪽을 제외하고
        # 그 다음 수부터 다시 같은 작업을 반복한다 (i = min(mi, ma)+1)
        # 이 때, 최소, 최댓값의 인덱스는 작업을 재개하는 인덱스로 재설정하며 부분수열의 길이도 0으로 초기화한다
        if nums[ma] - nums[mi] > 2:
            i = min(mi, ma) + 1
            mi = ma = i
            dp[i - 1] = cnt
            cnt = 0
        else:
            i += 1
            cnt += 1

    # 마지막에 구한 부분수열의 길이는 dp에 저장되어있지 않기 때문에 별도로 계산해준다
    print(max(*dp, cnt))
