class Solution:
   def moveZeroes(self, nums: List[int]) -> None:
      """
      Do not return anything, modify nums in-place instead.
      """
        
      i = 0
        
      for n in nums:
         if n != 0: 
            nums[i] = n
            i += 1
        
      nums[i:] = (len(nums)-i)*[0]