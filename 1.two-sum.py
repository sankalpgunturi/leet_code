class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_list = []

        new_nums = nums.sort()

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
            return [final_list.index(final_list[0]), final_list.index(final_list[1])]

        elif target < nums[len(nums) - 1]:
            digit = closest(nums, target)
            add_digits(digit)
            final_list.append(digit)
            return [final_list.index(final_list[0]), final_list.index(final_list[1])]

        else:
            return [nums[0], [len(nums) - 1]]
