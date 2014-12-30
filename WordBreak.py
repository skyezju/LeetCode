class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean
    def wordBreak2(s, dict):
        checkStatus = [False]*(len(s)+1)
        checkStatus[0] = True
        for i in range(len(s)):
            if not checkStatus[i]:
                continue
            for tempdict in dict:
                dictend = 0
                dictend = i + len(tempdict)
                if dictend > len(s):
                    continue
                if checkStatus[dictend]:
                    continue
                if tempdict == s[i:dictend]:
                    checkStatus[dictend]=True

        return checkStatus[len(s)]



