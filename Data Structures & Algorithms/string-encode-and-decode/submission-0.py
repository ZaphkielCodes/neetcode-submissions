class Solution:
    # Use an integer at the beginning of strs that represents the length of the word
    # And add a special character so your code doesnt break if the word begins with a int
    # for example if the word is "4code" we can use 5> to encode 5 is the length of the word
    # and > is the separator

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_str += str(len(word)) + ">" + word
        
        return encoded_str

    











    def decode(self, s: str) -> List[str]:
        # ptr 1 starts at the beginning
        # ptr 2 starts at ptr 1 and moves right until ptr 2 finds the separator
        # slice off everything in between (that is the int representing the length)
        # words is everything between (ptr 2) + 1 and (ptr 2) + 1 + the length which starts right after ptr 2
        # then set ptr 1 right after that
        # repeat

        # i is pointer 1, j is pointer 2
        i = 0
        result = []

        while i < len(s):
            j = i

            while s[j] != ">":
                j += 1
            
            length = int(s[i:j])
            word = s[j+1: j+1+length]
            result.append(word)

            i = j+1+length

        return result








        