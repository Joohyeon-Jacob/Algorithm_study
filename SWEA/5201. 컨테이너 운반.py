import sys
sys.stdin = open('sample_input_컨테이너 운반.txt', 'r')

# 테스트 케이스
T = int(input())

for tc in range(1, T+1):
    # N : 컨테이너 수 / M : 트럭 수
    N, M = map(int, input().split())

    # 각 컨테이너의 무게
    container_weight = list(map(int, input().split()))

    # 각 트럭의 적재용량
    weight_capability = list(map(int, input().split()))

    container_weight.sort(reverse=True)
    weight_capability.sort()

    # 운반한 무게
    result = 0

    for i in range(len(container_weight)):
        for j in range(len(weight_capability)):
            if container_weight[i] <= weight_capability[j]:
                # 운반한 무게에 추가
                result += container_weight[i]
                # 무게 목록에서 제거 & 적재 가능 트럭에서 제거(한 개만 적재 가능!!)
                container_weight[i] = 0
                weight_capability[j] = 0
                break

    print(f'#{tc} {result}')