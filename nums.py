def find_missing_nums(nums):
    number = input()
    nums = number.split()
    nums = list(map(int, nums))
    nums.sort()
    chislo = nums[-1]
    ustal = [x for x in range(1, chislo + 1)]
    missing = []

    for value in ustal:
        if value in nums:
            continue
        else:
            missing.append(value)
    return missing

print(find_missing_nums(nums))
