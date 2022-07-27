import sys

input = sys.stdin.readline


# 2064 IP 주소
# n개의 IPv4 주소가 주어졌을 때 네트워크 주소와 서브넷 마스크를 구하는 문제
# 가능한 케이스가 여러개라면 서브넷 범위가 가장 작은 것을 구한다.
def sol2064():
    # 최소, 최대 IP주소를 구함
    min_address = [255, 255, 255, 255]
    max_address = [0, 0, 0, 0]
    for _ in range(int(input())):
        ip = list(map(int, input().split('.')))
        min_address = min(min_address, ip)
        max_address = max(max_address, ip)

    # 두 IP의 비트가 처음으로 달라지는 부분 전까지 서브넷 마스크의 비트가 1일 수 있음
    subnet_mask = [0, 0, 0, 0]
    idx = 0
    while idx < 4 and min_address[idx] == max_address[idx]:
        subnet_mask[idx] = 255
        idx += 1

    if idx < 4:
        bit = 128
        while bit > 0:
            if bit & min_address[idx] == bit & max_address[idx]:
                subnet_mask[idx] += bit
                bit //= 2
            else:
                break

    # 서브넷 마스크로 네트워크 주소 획득
    net_address = [min_address[i] & subnet_mask[i] for i in range(4)]

    return '\n'.join(['.'.join(map(str, net_address)), '.'.join(map(str, subnet_mask))])
