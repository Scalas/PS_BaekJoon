import sys
from bisect import bisect_right

input = sys.stdin.readline
INF = 40000000


# 9007 카누 선수
# 네 개의 클래스의 학생 각 n명의 몸무게와 이상적인 몸무게합 k가 주어졌을 때
# 네 클래스에서 한명씩의 학생을 뽑아 그 몸무게를 더한 값중 가장 k에 가까운 값을 구하는 문제
# 만약 k와의 차이가 같다면 보다 작은값을 우선시 
def sol9007():
    answers = []
    for _ in range(int(input())):
        k, n = map(int, input().split())
        c1 = list(map(int, input().split()))
        c2 = list(map(int, input().split()))
        c3 = list(map(int, input().split()))
        c4 = list(map(int, input().split()))

        # c1, c2에서 한명씩을 뽑아 만들 수 있는 몸무게의 합과 c3, c4에서 한명씩을 뽑아 만들 수 있는 몸무게의 합을 각각 구함
        # 중복값은 필요하지 않기 때문에 set을 사용
        g1 = set()
        g2 = set()
        for w1 in c1:
            for w2 in c2:
                g1.add(w1 + w2)
        for w1 in c3:
            for w2 in c4:
                g2.add(w1 + w2)
                
        # g2를 정렬
        g2 = sorted(g2)

        # k에서 g1의 무게를 뺀 값에 가장 근사한 값을 g2에서 찾고
        # g1과 그 값의 합이 기존 무게의 합보다 k에 가깝다면 갱신
        answer = -1
        diff = INF
        for w1 in g1:
            idx = bisect_right(g2, k - w1)
            if idx > 0:
                w = w1 + g2[idx-1]
                d = abs(w - k)
                if d < diff or (d == diff and w < answer):
                    answer = w
                    diff = d
            if idx < len(g2):
                w = w1 + g2[idx]
                d = abs(w - k)
                if d < diff or (d == diff and w < answer):
                    answer = w
                    diff = d

            # 더이상 차가 좁혀질 수 없다면(차이가 0) break
            if not diff:
                break

        answers.append(answer)

    return '\n'.join(map(str, answers))
