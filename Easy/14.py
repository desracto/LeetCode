# Easy: 14
def longestCommonPrefix(self, strs:list[str]) -> str:
    # sort input string list
    # check the prefix list of the first & last string
    # stop at the lowest one
    ans = ""
    sorted_strs = sorted(strs)
    first_str = sorted_strs[0]
    last_str = sorted_strs[-1]

    for i in range(min(len(first_str), len(last_str))):
        if first_str[i] != last_str[i]:
            return ans
        ans += first_str[i]
    
    return ans