class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_list = []

        new_nums = nums.copy()
        new_nums.sort()

        def add_digits(digit):
            i = len(new_nums) - 2
            while i >= 0:
                if target == digit + new_nums[i]:
                    return final_list.append(new_nums[i])

                else:
                    i = i - 1

        def closest(lst, K):

            return lst[min(range(len(lst)), key = lambda i: abs(lst[i]-K))]

        if target > new_nums[len(new_nums) - 1]:
            digit = new_nums[len(new_nums) - 1]
            add_digits(digit)
            final_list.append(digit)
            print(nums, nums.index(final_list[0]), nums.index(final_list[1]))
            if final_list[0] != final_list[1]:
                return [nums.index(final_list[0]), nums.index(final_list[1])]
            else:
                value = nums.index(final_list[0])
                return [value, value + 1]


        elif target < new_nums[len(new_nums) - 1]:
            digit = closest(new_nums, target)
            add_digits(digit)
            final_list.append(digit)
            if final_list[0] != final_list[1]:
                return [nums.index(final_list[0]), nums.index(final_list[1])]
            else:
                value = nums.index(final_list[0])
                return [value, value + 1]

        else:
            return [nums[0], [len(nums) - 1]]
