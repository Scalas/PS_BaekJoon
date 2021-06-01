import sys

input = sys.stdin.readline


# 1920 수 찾기
# 배열 A에 특정 수의 포함여부를 알아내는 문제

# 가장 기본적인 풀이는 이분탐색을 활용한 풀이
# 배열 A를 정렬하는데 O(NlogN)
# M개의 숫자를 탐색하는데 각각 logN씩 O(MlongN)
def sol1920():
    input()
    a = list(map(int, input().split()))
    a.sort()
    input()
    answer = []
    for num in list(map(int, input().split())):
        answer.append('1' if search(a, 0, len(a)-1, num) else '0')
    sys.stdout.write('\n'.join(answer))


def search(arr, s, e, t):
    while(s<=e):
        mid = (s+e)//2
        if(arr[mid]==t):
            return True
        elif(arr[mid]<t):
            s = mid+1
        else:
            e = mid-1
    return False


# 파이썬의 경우 set 자료구조를 활용하여 더 쉽게 풀 수 있다.
# set 자료구조는 중복을 제거하는 데도 유용하지만
# in 연산의 복잡도가 O(1)이란 이점 또한 있다.
# 배열 A의 요소들을 set 에 삽입하는데 O(N) (set 의 삽입, 삭제, 탐색, 포함여부 연산은 모두 O(1))
# M개의 숫자를 탐색하는데 각각 O(1)씩 O(M)
def sol1920_2():
    input()
    a = set(map(int, input().split()))
    input()
    answer = []
    for num in list(map(int, input().split())):
        answer.append('1' if num in a else '0')
    sys.stdout.write('\n'.join(answer))
