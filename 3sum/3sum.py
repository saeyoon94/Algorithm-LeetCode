class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        result = set()

        nums.sort()

        for i in range(len(nums) - 1):
            temp_arr = nums[i + 1:]

            start = 0
            end = len(temp_arr) - 1

            while start < end:
                temp_sum = nums[i] + temp_arr[start] + temp_arr[end]
                if temp_sum == 0:
                    result.add((nums[i], temp_arr[start], temp_arr[end]))
                    start += 1
                elif temp_sum > 0:
                    end -= 1
                else:
                    start += 1

        return list(result)
            
        