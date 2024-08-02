import sys
from collections import defaultdict
input=sys.stdin.readline

N=int(input())

nums = defaultdict(int)
for i in range(N):
    nums[int(input())] += 1

for i in sorted(nums):
    for j in range(nums[i]):
        print(i)