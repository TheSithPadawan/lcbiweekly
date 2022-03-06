# problem: https://leetcode.com/problems/sort-the-jumbled-numbers/

"""
Algo:
- process each number using 进制转换 log(num) time
- then sort O(nlogn)
data scale 1e5 works fine
Any string processing algo should totally time out due to each number is 1e9
"""


class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        temp = [] # stores (converted value, index)
        for i, n in enumerate(nums):
            # convert n
            if n == 0:
                temp.append((mapping[n], i))
                continue
            t = 1
            newnum = 0
            while n:
                digit = n % 10
                newnum = mapping[digit] * t + newnum
                n //= 10 # integer division, otherwise runs into big trouble
                t *= 10
            temp.append((newnum, i))
        temp = sorted(temp, key=lambda x: (x[0], x[1]))
        result = [nums[x[1]] for x in temp]
        return result