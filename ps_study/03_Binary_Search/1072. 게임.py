
import sys

if __name__ == "__main__":
    X, Y = map(int, sys.stdin.readline().split())

    Z = (Y * 100) // X
    left = 0
    right = X
    result = X

    if Z >= 99:
        print(-1)

    else:
        while left <= right:
            mid = (left+right) // 2
            if ((Y+mid) * 100) // (X+mid) > Z:
                result = mid
                right = mid - 1
            else:
                left = mid + 1

        print(result)
