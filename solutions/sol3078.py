import sys

input = sys.stdin.readline


# 3078 좋은 친구
# 학생의 이름이 성적순으로 주어지고 등수 차이가 k 이하이고
# 이름이 같은 길이인 학생끼리만 좋은 친구라고 할 때
# 좋은 친구 쌍의 갯수를 구하는 문제
def sol3078():
    n, k = map(int, input().split())

    # 이름 길이가 같은 그룹끼리 구분
    name_groups = [[] for _ in range(21)]
    for i in range(n):
        name_groups[len(input().rstrip())].append(i)

    # 이름 길이가 같은 그룹 내에서 성적차가 k 이하인 친구 쌍의 수를 더하여 반환
    answer = 0
    for group in name_groups:
        s = e = 0
        pair = 0
        while e < len(group) - 1:
            if group[e + 1] - group[s] <= k:
                e += 1
                pair += 1
            else:
                answer += pair
                s += 1
                pair -= 1
        answer += ((e - s) * (e - s + 1) // 2)

    return answer
