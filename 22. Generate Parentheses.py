class Solution:
    def generateParenthesis(self, n):
        ans=[]
        self.helper(n,n,'',ans)
        return ans
    def helper(self,openBracket,closedBracket,path,ans):
        if closedBracket==0 and openBracket==0:
            return ans.append(path)
        if closedBracket>0 and openBracket < closedBracket:
            self.helper(openBracket,closedBracket-1,path+")",ans)
        if openBracket>0:
            self.helper(openBracket-1,closedBracket,path+"(",ans)
s=Solution()
print(s.generateParenthesis(3))