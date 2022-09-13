import sys

input = sys.stdin.readline


# 6590 덧셈 체인
# n에 대한 덧셈체인 An의 각 원소 ai 는 다음 조건을 만족
# 1. a0 = 1
# 2. am = n
# 3. a0 < a1 < a2 < ... < am-1 < am
# 4. 각각의 k(1 ≤ k ≤ m)에 대해서, ak = ai + aj를 만족하는 두 자연수(같아도 됨) i와 j가 존재 (0 ≤ i, j ≤ k-1)
# 100 이하의 양의 정수 n이 주어졌을 때, An 이 될 수 있는 수열 하나를 구하는 문제
def sol6590():
    answers = []

    # 가장 짧은 덧셈 체인의 idx 번째 숫자를 구하는 함수
    def dfs(idx):
        nonlocal answer, chain, n, min_len

        # 덧셈 체인을 완성한 경우 가장 짧은 덧셈 체인의 길이와 idx 번째 숫자를 갱신
        if chain[-1] == n:
            answer[idx] = chain[-1]
            min_len = len(chain)
            return True

        # 덧셈 체인을 완성하지 못하고 체인의 길이가 min_len을 넘긴 경우 탐색을 중지
        if idx == min_len - 1:
            return False

        # 다음 숫자로 가능한 후보에 대해 탐색
        i = len(chain) - 1
        update = 0
        while i >= 0:
            j = i
            while j >= 0:
                num = chain[i] + chain[j]
                if num <= chain[-1]:
                    break

                if num <= n:
                    chain.append(num)
                    check = dfs(idx + 1)
                    chain.pop()
                    if check:
                        answer[idx] = chain[-1]
                        update += 1
                j -= 1
            i -= 1

        return True if update else False

    # 모든 테스트 케이스에 대해 최단 덧셈 체인을 구함
    while True:
        n = int(input())
        if not n:
            break

        if n <= 3:
            answers.append(' '.join(map(str, range(1, n + 1))))
            continue

        answer = [i for i in range(1, n + 1)]
        min_len = n
        chain = [1]
        dfs(0)

        answers.append(' '.join(map(str, answer[:min_len])))

    return '\n'.join(answers)
