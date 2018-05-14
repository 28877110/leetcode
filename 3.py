class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = {}
        st = -1
        maxLength = 0
        for i, ch in enumerate(s):
            if ch not in a:
                a[ch] = i
                tem = i - st
                if tem > maxLength:
                    maxLength = tem
            elif st > a[ch]:
                a[ch] = i
                tem = i - st
                if tem > maxLength:
                    maxLength = tem
            else:
                st = a[ch]
                a[ch] = i
        return maxLength

a = Solution()
re = a.lengthOfLongestSubstring("tmmzuxt")
print(re)