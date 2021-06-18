from sys import stdin, stdout


# 10989 수 정렬하기 3
# n의 수가 1000만까지 늘어나 O(NlogN)으론 풀 수 없는 수준
# 수의 범위가 1에서 10000으로 작기에 카운팅정렬을 활용해야한다

# 메모리 제한이 8 MB 이므로 입력받을 수를 모두 리스트에 저장해둘 수 없기때문에
# stdin.readline 을 n번 호출하거나 stdin 에 들어있는 line을 직접 순회하여 작업해야한다
# 마찬가지로 출력 또한 리스트에 담아두고 출력하는 방식은 사용할 수 없기때문에
# stdout에 쓰는 방식을 취해야한다
def sol10989():
    stdin.readline()
    counts = [0]*10001
    for num in stdin:
        counts[int(num)] += 1
    for i in range(1, 10001):
        stdout.write(f'{i}\n' * counts[i])
