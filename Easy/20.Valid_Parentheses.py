class Solution:
    def isValid(self, s):
        if s == "":
            return True
        u = ['(', '{', '[']
        d = [')', '}', ']']
        tmp = list()
        for char in s:
            if char in u:
                i = u.index(char)
                tmp.append(d[i])
            if char in d and char in tmp:
                tmp.pop()
            elif char in d and char not in tmp:
                return False
        return tmp == []
# Runtime: 32 ms, faster than 37.05% (2020/02/20)
# Memory Usage: 12.8 MB, less than 100.00% (2020/02/20)


class Solution_2:
    def isValid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for char in s:
            # If the character is an closing bracket
            if char in mapping:
                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'
                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)
        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack
# Runtime: 32 ms, faster than 37.05% (2020/02/20)
# Memory Usage: 12.8 MB, less than 100.00% (2020/02/20)
