import sys

input = sys.stdin.readline


# 22988 재활용 캠페인
# n개의 헤어에센스병에 든 헤어에센스의 양과 병의 최대용량 x가 주어지고
# 용량이 a인 헤어에센스와 b인 헤어에센스를 교환하면 (a + b + x/2) 만큼으로 교환해준다 할 때
# 최대용량의 헤어에센스를 최대 몇 개 만들 수 있는지 구하는 문제
# 단, 교환시 a + b + x/2 가 최대용량 x를 넘는다면 최대용량 x까지만 꽉 채워준다.
def sol22988():
    n, x = map(int, input().split())

    # 헤어에센스를 용량순으로 오름차순 정렬
    seq = list(map(int, input().split()))
    seq.sort()

    # 만들 수 있는 꽉찬 헤어에센스 용기
    answer = 0

    # 이미 꽉찬 헤어에센스 제거, 만들 수 있는 꽉찬 헤어에센스 용기 추가
    while seq and seq[-1] == x:
        seq.pop()
        answer += 1
        n -= 1

    # 용량 x의 절반
    half = x / 2

    # 교환 방식상 두 헤어에센스의 합이 x의 절반 이상이라면 꽉찬 헤어에센스로 교환 가능
    # 교환 방식상 세 헤어에센스는 반드시 꽉찬 헤어에센스로 교환 가능
    # 즉, 두 개의 헤어에센스만으로 꽉찬용기를 최대한 만드는 것이 최적

    # 최소 헤어에센스와 최대 헤어에센스의 인덱스
    s, e = 0, n-1

    # 남아있는 어느 헤어에센스와 조합해도 꽉찬 헤어에센스를 만들 수 없는 헤어에센스의 갯수
    remain = 0

    while s < e:
        # 헤어에센스 s와 e를 조합해서 꽉찬 헤어에센스를 만들 수 있다면
        # 두 에센스로 꽉찬 헤어에센스 하나를 교환하고 각 인덱스를 증감시킴
        if seq[s] + seq[e] >= half:
            answer += 1
            s += 1
            e -= 1

        # 만들 수 없다면 최소 헤어에센스쪽은 이제 어느 헤어에센스와 조합해도
        # 꽉찬 헤어에센스를 만들 수 없음. remain을 하나 추가하고 인덱스 증가
        else:
            remain += 1
            s += 1

    # 만약 s == e 에서 반복문이 끝났다면 그 지점의 헤어에센스도 remain에 추가
    if s == e:
        remain += 1

    # 남은 헤어에센스들은 반드시 3개를 합쳐야만 하나의 꽉 찬 헤어에센스로 교환할 수 있음
    answer += remain // 3

    return answer
