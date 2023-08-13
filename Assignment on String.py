class Soloution:
    def isValid(self,s):
        stack = []
        brackets = {'(': ')', '[': ']', '{': '}'}

        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack or brackets[stack.pop()] != char:
                    return False

        return len(stack) == 0

# Test cases
print(Soloution().isValid("()"))          # Output: True
print(Soloution().isValid("()[]{}"))      # Output: True
print(Soloution().isValid("(]"))          # Output: False
print(Soloution().isValid("(())"))        # Output: True
print(Soloution().isValid("(()"))         # Output: False


# Time Complexity: O(n)
# Space Complexity: O(n)