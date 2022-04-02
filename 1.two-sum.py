nums = [2, 7, 11, 15]
target = 9
final_list = []

nums.sort()

def add_digits(digit):
    i = len(nums) - 2
    while i >= 0:
        if target == digit + nums[i - 1]:
            return final_list.append(nums[i - 1])

        else:
            i = i - 1

def closest(lst, K):

    return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

if target > nums[len(nums) - 1]:
    digit = nums[len(nums) - 1]
    add_digits(digit)
    final_list.append(digit) 

elif target < nums[len(nums) - 1]:
    digit = closest(nums, target)
    add_digits(digit)
    final_list.append(digit)

else:
    final_list.append(nums[0])
    final_list.append([len(nums) - 1])

for i in range(0, len(final_list)):

    print(final_list)