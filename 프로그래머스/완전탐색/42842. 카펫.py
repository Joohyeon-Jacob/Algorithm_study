
def solution(brown, yellow):
    # yellow 감싸는 타일 개수 // 2
    cover_yellow = (brown-4) // 2

    for i in range(int(cover_yellow**0.5), cover_yellow+ 1):
        if i >= cover_yellow-i and i * (cover_yellow - i) == yellow:
            answer = [i+2, cover_yellow-i+2]
            break
    return answer
