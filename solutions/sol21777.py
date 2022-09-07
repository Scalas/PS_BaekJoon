import sys

input = sys.stdin.readline


# 21777 리버스 가희와 프로세스 1
# 스케줄러는 다음 두 가지 기준에 따라 매 초마다 실행할 프로세스를 정한다.
# 1. 우선순위 값이 가장 큰 프로세스
# 2. 우선순위 값이 같다면 id가 가장 작은 프로세스
# 이 기준에 따라 스케줄러가 t초간 실행한 프로세스의 순서가 주어졌을 때
# 스케줄러에 의해 실행된 프로세스들의 우선순위와 실행시간을 구하는 문제
# 답이 여러개라면 그중 하나만 출력해도 무방
def sol21777():
    t = int(input())

    # 프로세스 실행시간
    process_runtime = dict()

    # 우선순위가 자신 다음으로 높은 프로세스와의 우선순위 차이
    priority_difference = dict()

    # 우선순위가 자신 다음으로 높은 프로세스의 id
    pre_pid = -1

    for pid in map(int, input().split()):
        # 이미 실행한 적이 있는 프로세스일 경우
        if pid in process_runtime:
            process_runtime[pid] += 1

        # 처음 실행된 프로세스일 경우
        else:
            if pre_pid != -1:
                # 현재 프로세스의 id가 pre_pid보다 작다면 pre_pid 프로세스가 실행된 횟수 만큼의 우선순위 차이가 남
                if pid < pre_pid:
                    priority_difference[pid] = process_runtime[pre_pid]

                # 현재 프로세스의 id가 pre_pid보다 크다면 pre_pid 프로세스가 실행된 횟수보다 1 적은 만큼의 우선순위 차이가 남
                else:
                    priority_difference[pid] = process_runtime[pre_pid] - 1
            else:
                priority_difference[pid] = 0
            
            # 프로세스의 실행시간을 1 늘리고 pre_pid 갱신
            process_runtime[pid] = process_runtime.get(pid, 0) + 1
            pre_pid = pid

    # process_runtime 에 삽입된 순서가 곧 우선순위가 높은 순서이므로
    # 우선순위가 높은 프로세스부터 순차적으로 우선순위를 계산한 뒤 pid기준으로 정렬
    answers = []
    priority = t + 1
    for pid, runtime in process_runtime.items():
        priority = priority - priority_difference[pid]
        answers.append([pid, runtime, priority])
    answers.sort()
    
    # 실행된 프로세스의 갯수와 각 프로세스의 pid, 실행시간, 우선순위를 반환 
    return str(len(process_runtime.keys())) + '\n' + '\n'.join([' '.join(map(str, answer)) for answer in answers])
