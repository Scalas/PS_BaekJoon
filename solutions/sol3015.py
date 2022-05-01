import sys

input = sys.stdin.readline


# 3015 오아시스 재결합
# n명의 사람의 키가 순서대로 주어질 때
# 그중 두 사람을 뽑아 서로가 볼 수 있는 경우의 수를 구하는 문제
# 두사람이 서로를 보기 위해서는 두 사람 사이에 둘 중 하나보다 키가 큰 사람이 없어야 함
def sol3015():
    n = int(input())
    heights = [int(input()) for _ in range(n)]
    st = []
    answer = 0
    for _ in range(n):
        # 현재 사람의 키
        h = int(input())
        
        # 현재 사람보다 키가 이전 사람의 키보다 큰동안
        # 이전 사람을 스택에서 pop 하고 그 수만큼 볼 수 있는 쌍을 늘림
        while st and st[-1][0] < h:
            answer += st.pop()[1]
            
        # 만약 현재 사람과 키가 같거나 큰 사람이 남아있다면
        if st:
            # 현재 사람보다 키가 큰 사람이 하나라도 있다면 볼 수 있는 쌍 1개 증가
            if st[0][0] > h:
                answer += 1
                
            # 이전 사람의 키가 자신과 같다면 키가 같은 사람의 수만큼 볼 수 있는 쌍을 늘리고
            # 키가 같은 사람의 수를 하나 늘림
            if st[-1][0] == h:
                answer += st[-1][1]
                st[-1][1] += 1
                
            # 이전 사람의 키가 자신보다 크다면 스택에 삽입 
            else:
                st.append([h, 1])
        
        # 이전 사람이 남아있지 않다면 스택에 삽입
        else:
            st.append([h, 1])

    return answer
