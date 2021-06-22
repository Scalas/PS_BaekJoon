from sys import stdin


# 5086 배수와 약수
# 두 수의 관계를 구하는 문제
# 첫 번째 숫자가 두 번째 숫자의 약수이다. = factor
# 첫 번째 숫자가 두 번째 숫자의 배수이다. = multiple
# 첫 번째 숫자가 두 번째 숫자의 약수와 배수 모두 아니다. = neither
def sol5086():
    res = ['neither', 'factor', 'multiple']
    answer = []
    for i in stdin:
        n, m = map(int, i.split())
        if n == m == 0:
            break
        answer.append(res[(m % n == 0) + 2 * (n % m == 0)])
    print('\n'.join(answer))
