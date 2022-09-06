import sys

input = sys.stdin.readline


# 6198 옥상 정원 꾸미기
# n개의 빌딩의 높이가 왼쪽부터 순서대로 주어지고 각 빌딩의 옥상에서
# 오른쪽 빌딩중 자신보다 높이가 낮은 빌딩의 옥상만을 볼 수 있으며
# 자신보다 높은 빌딩이 나타난 이후의 빌딩은 볼 수 없을 때
# 각 빌딩의 옥상에서 볼 수 있는 다른 빌딩의 옥상의 수의 합을 구하는 문제
def sol6198():
    n = int(input())
    buildings = [int(input()) for _ in range(n)][::-1]
    st = []
    answer = 0
    for b in buildings:
        count = 0
        # 자신보다 높은 건물을 만나기 전 까지 자신보다 낮은 건물의 수와
        # 그 건물들에서 볼 수 있는 건물 옥상의 수를 더한 값이 현재 건물에서 볼 수 있는 다른 건물의 옥상의 수
        while st and st[-1][0] < b:
            _, c = st.pop()
            count += (c + 1)
        answer += count
        st.append((b, count))
    return answer
