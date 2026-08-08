class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a new dictionary
        # loop through the strs from index 0 to length of strs
        # sort the string
        # every index use the sorted string as the key and the unsorted original string as the value
        #once done with the loop, put the keys into a sublist

        my_dict = {}
        for i in range(len(strs)):
            sorted_strs = tuple(sorted(strs[i]))
            if sorted_strs not in my_dict:
                my_dict[sorted_strs] = [strs[i]]
            else:
                my_dict[sorted_strs].append(strs[i])

        return list(my_dict.values())
