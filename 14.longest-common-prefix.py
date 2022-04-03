class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        else:
            same = ""
            for i in range(len(strs)):
                for j in range(0, len(strs[i])):
                    out = [x[0:(j + 1)] for x in strs]
                    for k in range(1, len(out)):
                        if out[0] == out[k]:
                            if k == (len(out) - 1):
                                same = out[k]
                        else:
                            break
                break


            return same