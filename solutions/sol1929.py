import sys
import math

input = sys.stdin.readline


# 1929 소수 구하기
# 에라스토테네스의 체를 활용하여 m에서 n 까지의 소수를 구하는 문제


# 에라스토테네스의 체를 적용하는 과정은 list comprehension 을 활용하여 간단하게 가능
# 단순히 2부터 n 까지의 정수 i 에서 nums[i] 의 값이 1인 것을 출력해도 되지만
# 짝수중에 정수는 없다는 점에 착안하여 m 이상의 홀수들 중에서만 nums[i]가 1인것을 출력하면
# 더 빠르게 답을 구할 수 있다.
# 단, 이 경우 m이 2 이하이고 n이 2 이상일 경우 2가 포함되지 않는 문제를 해결해줘야한다.
def sol11653():
    m, n = map(int, input().split())
    nums = [1]*(n+1)
    nums[1] = 0
    for i in range(2, int(math.sqrt(n))+1):
        if nums[i]==1:
            nums[i*2::i] = [0]*(n//i-1)
    print('\n'.join((['2'] if n>=2 and m<=2 else [])+[str(i) for i in range(m+1-m%2, n+1, 2) if nums[i]==1]))
