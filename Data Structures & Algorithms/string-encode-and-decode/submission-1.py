class Solution:
    def encode(self, strs: List[str]) -> str:
        # > is the separator
        encoded_str = ""
        for word in strs:
            # encode = length of the word + separator + actual word
            encoded_str += str(len(word)) + ">" + word  
        
        return encoded_str

    def decode(self, s: str) -> List[str]:

        # i is pointer 1, j is pointer 2
        i = 0
        result = []
    
        while i < len(s):
            j = i   # pointer 2 starts at pointer 1

            while s[j] != ">":  # pointer 2 looks for the length
                j += 1
            
            length = int(s[i:j])    # --> int representing the length of the word
            word = s[j+1: j+1+length]   # slice at j+1(the beginning of the word)
            result.append(word)

            i = j+1+length  # set pointer 1 at the end of the word

        return result








        