import sys


# 1181 단어 정렬
# 입력받은 단어들을 중복을 제거한 후 길이순으로 오름차순 정렬, 길이가 같다면 사전순으로 오름차순 정렬하는 문제
# 파이썬의 경우 set 으로 중복을 제거한 뒤 람다함수로 정렬기준을 전달하면 해결가능
def sol1181():
    n, *s = sys.stdin.read().splitlines()
    s = list(set(s))
    s.sort(key=lambda x: (len(x), x))
    print('\n'.join(s))
