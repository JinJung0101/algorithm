#nums = list(int, input().split())
nums = []
for i in range(9):
    nums.append(int(input()))
maxnum = nums[0]
maxnum_index = 0
for i in range(len(nums)):
    if nums[i] > maxnum:
        maxnum = nums[i]
        maxnum_index = i
print(maxnum)
print(maxnum_index+1)


# for i in range(0, len(nums)):
#     if nums[i] == maxnum:
#         print(i+1)

