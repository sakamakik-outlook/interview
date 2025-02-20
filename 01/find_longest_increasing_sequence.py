

# input = [1,2,3]
# output = [1,2,3]

# input = [1,2,2]
# output = [1,2]

# input = [1,2,3,2,9,10,11,12,13,6,7,8]
# output = [2,9,10,11,12,13]


# write a program to get the longest sequence

nums = [1,2,3,2,9,10,11,12,13,14,6,7,8,9,10,11,12,13,14,15]
longest_start = 0 
longest_end = 0
start = 0
end = 0

n = len(nums)
dp = [1] * n
prev = [-1] * n

max_length = 0
max_index = -1

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
            prev[i] = j
    if dp[i] > max_length:
        max_length = dp[i]
        max_index = i

lis = []
while max_index != -1:
    lis.append(nums[max_index])
    max_index = prev[max_index]

print(lis[::-1])



