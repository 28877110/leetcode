class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<=2:
            return s
        max = 0
        maxstart = 0
        length = len(s)
        for i in range(0,length-1):
            start,end = self.Palindrome(s,i,i)
            if max < end - start - 1:
                maxstart = start + 1
                max = end - start - 1
            start, end = self.Palindrome(s, i, i+1)
            if max < end - start - 1:
                maxstart = start + 1
                max = end - start - 1

        return s[maxstart:maxstart+max]

    def Palindrome(self,s,start,end):
        while start >=0 and end <len(s) and s[start] == s[end]:
            start-=1
            end+=1
        return start,end
a = Solution()
re = a.longestPalindrome('a')
print(re)