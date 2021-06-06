import sys
import heapq

input = sys.stdin.readline


# 1655 가운데를 말해요
# 힙을 활용한 중간값 찾기 문제

# 최소힙, 최대힙을 동시에 사용하면 해결 가능하다
# 중간값을 찾기 위해서 최소힙과 최대힙의 크기의 차는 2이상이 되어선 안되며
# 최대힙의 top 은 최소힙의 top 보다 작아야한다.
# 먼저 최대힙이 비어있다면 최대힙에 숫자를 넣고
# 그 이후부터는 최대힙의 top 보다 작거나 같은 수는 최대힙에, 큰 수는 최소힙에 삽입한다
# 둘의 크기 차이가 2가 될 경우 큰쪽을 하나 pop 하여 작은 쪽으로 push 하는 것으로 균형을 맞춘다
# 하나의 숫자가 삽입될 때마다 중간값은 두 힙중 크기가 큰쪽의 top, 두 힙의 크기가 같다면 최대힙의 top 이 된다
def sol1655():
    bh, sh = [], []
    answer = []
    for n in range(int(input())):
        num = int(input())
        if not bh:
            heapq.heappush(bh, -num)
        else:
            if(num<=-bh[0]):
                heapq.heappush(bh, -num)
            else:
                heapq.heappush(sh, num)
        if(len(bh)==len(sh)+2):
            heapq.heappush(sh, -heapq.heappop(bh))
        elif(len(sh)==len(bh)+2):
            heapq.heappush(bh, -heapq.heappop(sh))
        answer.append(str(-bh[0]) if len(bh) >= len(sh) else str(sh[0]))
    print('\n'.join(answer))