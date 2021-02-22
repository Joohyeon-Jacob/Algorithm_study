# A : 낮에 올라가는 거리 / B : 밤에 미끄러지는 거리 / V : 올라가야 할 나무 막대 높이

A, B, V = map(int, input().split())

import time
start = time.time()

# 걸린 일 수 계산
cnt = (V-A) // (A-B)

if (V-A) % (A-B) == 0: # cnt 일 수 만큼 오르내리고, 다음날 A 만큼 오르면 V 도착
    cnt += 1
else:
    cnt += 2
print(cnt)

# 걸린 일 수 계산
# cnt = 0

# while True:
#     # 하루 추가
#     cnt += 1
#     # 낮에 올라간 거리만큼 남은 높이 차감
#     V -= A
#     # 전체 높이 이상으로 낮에 올라가면 break
#     if V <= 0:
#         print(cnt)
#         break
#     # 낮에 올랐지만, 더 올라야 할 경우 밤에 미끄러지는 것 반영하기
#     else:
#         V += B

# 반복문을 사용하면 시간 초과 발생
# 구글링 힌트 : 마지막 순간을 확인해서 답 출력하면 시간 초과 문제 해결 가능

print(time.time()-start)