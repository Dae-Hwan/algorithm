

def twoSum(self, nums: List[int], target: int) -> List[int]:
    for index1 in range(len(nums)):
        num1 = nums[index1]
        for index2 in range(index1 + 1, len(nums)):
            num2 = nums[index2]
            if num1 + num2 == target:
                return [index1, index2]
