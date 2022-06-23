
import sys

n = int(sys.stdin.readline())
member_lst = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member_lst.append((age, name))

member_lst.sort(key = lambda x : x[0])	## (age, name)에서 age만 비교

for member in member_lst:
    print(member[0], member[1])
