
import sys

# 난쟁이 키 정보(2명은 거짓 난쟁이)
height_list = []

for _ in range(9):
    height = int(sys.stdin.readline())
    height_list.append(height)

height_list.sort()

# 키가 x1, x2 인 두 명 제외한 일곱 난쟁이의 키 합
def seven_height_sum(x1, x2):
    result = 0
    for k in range(9):
        if k not in [x1, x2]:
            result += height_list[k]

    return result

if __name__ == "__main__":
    # 제외할 두 명 선택
    for i in range(9):
        for j in range(i+1, 9):
            # 난쟁이 키 합이 100 맞춘 경우
            if seven_height_sum(i, j) == 100:
                fake_1, fake_2 = height_list[i], height_list[j]
                break

    for idx, num in enumerate(height_list):
        if num not in [fake_1, fake_2]:
            print(num)
