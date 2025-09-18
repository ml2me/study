#  https://stepik.org/lesson/1472696/step/2?thread=solutions&unit=1492407

def find_triple(nums):
    nums.sort()
    s = nums[-1]
    return [s - nums[2], s - nums[1], s - nums[0]]

print(find_triple([8, 5, 7, 4]))
print(find_triple([2, 2, 3, 2]))
print(find_triple([5, 3, 6, 4]))
print(find_triple([600000000, 600000000, 600000000, 900000000]))
print(find_triple([3, 5, 3, 4]))