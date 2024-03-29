class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == [""]:
            return ""
        first_word = strs[0]
        indexed_letters = None
        x = 0
        for index in range(0, len(first_word)+ 1):
            for words in strs[1:]:
                x += 1
                indexed_letters = words[0:index].find(first_word[0:index])
                print(index)

                if indexed_letters == -1:
                    return first_word[0 : index - 1]    
       
        return strs[0]

