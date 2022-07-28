class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        flag = True
        try:
            for n, char in enumerate(strs[0]):
                for str in strs[1:]:
                    if char != str[n]:
                        flag = False
                if flag:
                    output += char
            return output
        except:
            return output
# Runtime: 32 ms, faster than 67.43% (2020/02/20)
# Memory Usage: 12.8 MB, less than 100.00% (2020/02/20)

