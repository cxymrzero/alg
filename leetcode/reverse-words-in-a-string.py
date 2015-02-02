class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        l = s.split(' ')
        new_l = []
        for i in l:
            if i != '':
                new_l.append(i)
        new_s = ' '.join(new_l[::-1])
        return new_s

s = Solution()
print s.reverseWords("a")