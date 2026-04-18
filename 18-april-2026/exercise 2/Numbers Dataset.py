with open('numbers.txt', 'r') as f:
    nums = [int(line.strip()) for line in f]

print(nums)
print(sum(nums))
print(max(nums))
print(min(nums))
print(len([n for n in nums if n > 50]))