class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)    # placeholder to multiply it directly to the list
        pre_prod = 1
        suf_prod = 1

        for i in range (len(nums)):
            res[i] = pre_prod
            pre_prod *= nums[i]

        for i in range(len(nums) -1, -1, -1):
            res[i] *= suf_prod
            suf_prod *= nums[i]
        
        return res


        

















            # skip the number at current index and store everything else
            # slice method -> num[i:] grabs nums from before the current index and 
            # num[:i+1] grabs everything afer the current index

















        






        