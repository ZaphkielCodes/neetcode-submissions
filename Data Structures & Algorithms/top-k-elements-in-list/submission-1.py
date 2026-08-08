class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] not in my_dict:
                my_dict[nums[i]] = 1  
            else:
                my_dict[nums[i]] += 1

        # Note: .items() stores it in (key, value) pair
        # lambda specifies wether to sort the items using either key or value
        values = sorted(my_dict.items(), key = lambda items: items[1], reverse = True)
    
        key = []
        for vals in values[:k]:     # keep the first half of the sliced pairs 
            key.append(vals[0])
        
        return key


