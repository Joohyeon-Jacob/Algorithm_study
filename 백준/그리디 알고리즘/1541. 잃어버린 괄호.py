
if __name__ == "__main__":
    formula = input().split('-')
    # 최소 연산 결과
    result = 0

    for num in formula[0].split('+'):
        result += int(num)

    for num in formula[1:]:
        for basis in num.split('+'):
            result -= int(basis)

    print(result)