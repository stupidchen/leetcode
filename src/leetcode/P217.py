class Solution:
	def containsDuplicate(self, nums):
		"""
			:type nums: List[int]
			 :rtype: bool
			 """
			 if len(set(nums)) != len(nums):
				 return True
				 return False

