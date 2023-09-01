"""
В списке содержится список чисел строго по возрастанию.

Соберите в отдельный список те, которые НЕ содержатся в исходном списке.

Врен

def get_missed_between(numbers):
  pass

numbers = [100, 102, 104, 106, 107, 108, 110]

print(get_missed_between(numbers)) # вернет [101, 103, 105, 109]
"""

def get_missing_numbers(nums):
    missing_nums = []
    for num in nums:
        for i in range(1, len(nums)):
            if nums[i-1] > num:
                break
            else:
                missing_nums.append(num+1)
        return missing_nums

nums = [100, 102, 104, 106, 107, 108, 110]
missing_nums = get_missing_numbers(nums)
print(missing_nums) # [11, 21, 31, 41, 51, 61, 71, 81, 91]