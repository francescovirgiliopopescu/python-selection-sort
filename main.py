from typing import List

class SelectionSort:
  def sort(self, nums: List[int]):
    for i in range(len(nums) - 1):
      min_index = i
      for j in range(i + 1, len(nums)):
        if nums[min_index] > nums[j]:
          min_index = j
        nums[min_index], nums[i] = nums[i], nums[min_index]
      


nums = [8, 7, 9, 3, 2, 4, 1, 6, 5]

sort = SelectionSort()

sort.sort(nums)

print(nums)