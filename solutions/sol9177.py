import sys

input = sys.stdin.readline


# 9177 단어 섞기
# 단어 s1과 s2를 섞어서 s3를 만들 수 있는지 확인하는 문제
# 단, s1과 s2 각자의 문자들의 순서는 유지되어야한다.
def sol9177():
    n = int(input())

    # s1, s2가 각각 몇 번째 문자를 사용 가능한 상태인지 나타내는 i1, i2로 상태를 표현
    # 시간복잡도를 200 * 200 으로 한정
    def check(i1, i2):
        i3 = i1 + i2

        # s3을 완성한 경우 True 반환
        if i3 == len(s3):
            return True

        # 아직 확인해보지 않은 케이스인 경우
        if not visited[i1][i2]:
            # s3을 완성하기 전까지 반복
            while i3 < len(s3):
                # s1에서 문자를 가져올 수 있는 경우
                if i1 < len(s1) and s1[i1] == s3[i3]:
                    # 두 단어 모두에서 문자를 가져올 수 있는 경우
                    if i2 < len(s2) and s2[i2] == s3[i3]:
                        break

                    # s1의 인덱스를 1 증가, s3의 인덱스도 1 증가
                    i1 += 1
                    i3 += 1

                # s2에서 문자를 가져올 수 있는 경우
                # s2의 인덱스를 1 증가, s3의 인덱스도 1 증가
                elif i2 < len(s2) and s2[i2] == s3[i3]:
                    i2 += 1
                    i3 += 1

                # 두 단어 모두에서 문자를 가져올 수 없는 경우
                # s3를 만들 수 없음
                else:
                    return False

            # s3를 완성한 경우
            if i3 == len(s3):
                return True

            # 두 단어 모두에서 문자를 가져올 수 있는 경우
            # 재귀로 두 케이스를 모두 확인
            if check(i1 + 1, i2):
                return True

            if check(i1, i2 + 1):
                return True

            # s3를 만들지 못한경우 현재 케이스를 방문처리
            visited[i1][i2] = True
        return False

    answer = []
    # 케이스별로 yes or no 를 구함
    for _ in range(n):
        s1, s2, s3 = input().split()
        visited = [[False] * 201 for _ in range(201)]
        answer.append('yes' if check(0, 0) else 'no')

    return '\n'.join([f'Data set %d: %s' % (i + 1, answer[i]) for i in range(n)])
