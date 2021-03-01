class Solution:
    def groupAnagrams(self, strs):
        dict={}
        for i in strs:
            sorted_word="".join(sorted(i))
            if sorted_word not in dict:
                dict[sorted_word]=[i]
            else:
                dict[sorted_word].append(i)
        print(dict)
        res=[]
        for i in dict.values():
            res.append(i)
        print(sorted(res))
strs = ["eat","tea","tan","ate","nat","bat"]
s=Solution()
s.groupAnagrams(strs)