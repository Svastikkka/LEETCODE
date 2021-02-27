from random import sample


class Solution:

    def __init__(self, nums):
        self.origin = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        """
        return sample(self.origin, len(self.origin))

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
s=Solution([1,2,3,4,5,6,7])
print(s.shuffle())