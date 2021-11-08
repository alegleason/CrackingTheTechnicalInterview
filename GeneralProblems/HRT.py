
class Solution:
    def solution(self, S):
        # recursively check for new combinations so we return a string that cannot be further transformed
        while True:
            rec_s = self.getNewString(S)
            if rec_s != S:
                S = rec_s
            else:
                break
        return S

    def getNewString(self, S):
        # Base case
        if len(S) == 1:
            return S
        # O(n) time complexity and space complexity
        s_list = list(S)
        ret_s = ""
        i = 0
        # Apply as most transformations as we can
        while i < len(s_list) - 1:
            if not ((s_list[i] == 'A' and s_list[i + 1] == 'B') or (s_list[i] == 'B' and s_list[i + 1] == 'A') or (
                    s_list[i] == 'C' and s_list[i + 1] == 'D') or (s_list[i] == 'D' and s_list[i + 1] == 'C')):
                ret_s += s_list[i]
                if (i + 1) == len(s_list) - 1:
                    ret_s += s_list[i+1]
            else:
                i += 1
            i += 1
        # Append last char if it wasn't touched
        return ret_s


sol = Solution()
print(sol.solution("CBACD"))
print(sol.solution("CABABD"))
print(sol.solution("ACBDACBD"))



