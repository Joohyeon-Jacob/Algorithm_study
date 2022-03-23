import heapq


def solution(jobs):
    # answer : 답
    # cnt_time : 현재 위치한 시간
    # 처리한 작업의 개수
    answer, cnt_time, i = 0, 0, 0

    # 가장 최근에 처리한 작업의 처리 시작 시간
    start = -1

    # 요청이 들어온 작업들을 담아두는 최소 힙
    process = []

    # 모든 작업 처리할 때 까지 반복
    while i < len(jobs):
        # 현재 시간인 cnt_time(가장 최근 작업 처리 끝나고 난 시간)과
        # 가장 최근에 처리된 작업의 처리 시작 시간인 start에 대해,
        # 가장 최근 작업을 처리하는 동안 요청이 들어온 작업이 있는 지
        # 탐색하고 그 것들을 힙에 넣어두는 구문
        for job in jobs:
            if start < job[0] <= cnt_time:
                heapq.heappush(process, (job[1], job[0]))

        # 만약 힙에 처리해야 할 작업이 있는 경우 처리
        # 없다면 그냥 시간 1ms 더해줌
        # 우선순위가 높은 작업을 힙에서 꺼내고,
        # 이 구문에서 현재 꺼낸 작업을 처리하고,
        # 소요 시간을 answer에 더하고,
        # 곧바로 작업 끝나는 지점의 시간으로 점프하는 작업을 할 것임.
        # 따라서, start를 현재 위치로 정하고(뽑은 작업의 처리 시작 시간)
        # cnt_time을 처리 종료 시점인 (cnt_time + 현재 작업 소요 시간)으로 설정
        # 이러고 나면 이제, 뽑은 작업을 처리시키고 시간도 계산해낸 다음
        # 곧바로 다음 작업을 뽑아서 처리하고자 하는 상태가 되게 된다.
        if process:
            job = heapq.heappop(process)
            start = cnt_time
            cnt_time += job[0]
            answer += cnt_time - job[1]
            i += 1
        else:
            cnt_time += 1

    return answer // len(jobs)