import sys

input = sys.stdin.readline


# 15489 파스칼 삼각형
# r, c, w가 주어졌을 때 파스칼 삼각형의 r행 c열의 숫자를 꼭지점으로 하고
# 한 변에 포함된 숫자가 w개인 삼각형 안의 모든 숫자를 더한 값을 구하는 문제
def sol15489():
    r, c, w = map(int, input().split())
    r, c = r-1, c-1

    # 파스칼 삼각형의 왼쪽변
    pascal = [1] * (r+w)
    answer = 0

    # 왼쪽변은 오른쪽으로 한칸 갈때마다 이전단계의 누적합과 같아짐
    # 열 수만큼 누적합을 구하여 합을 구하려는 삼각형의 왼쪽변을 구함
    for i in range(c):
        for j in range(1, r+w):
            pascal[j] += pascal[j-1]
        r -= 1

    # 삼각형의 변의 길이만큼 누적합을 구하며 삼각형에 포함되는만큼을 합산
    for i in range(w):
        answer += sum(pascal[r:r+w-i])
        for j in range(1, r+w-i):
            pascal[j] += pascal[j-1]
    return answer
