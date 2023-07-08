# Easy: 28
def same(str1:str, str2:str, len):
    i = len-1
    while str1[i] == str2[i]:
        if i == 0:
            return True
        i = i - 1
    return False
def strStr(haystack: str, needle: str) -> int:
    """
        Makes use of Horspool algorithm
    """
    # Make Shift table
    shift = [None] * 57
    for i in range(0, len(shift)):
        shift[i] = len(needle)    
    for i in range(0, len(needle) - 1):
        shift[ord(needle[i]) - 65] = len(needle) - 1 - i

    # move through string and keep checking
    skip = 0
    while len(haystack) - skip >= len(needle):
        if same(haystack[skip:], needle, len(needle)):
            return skip
        skip = skip + shift[ord(haystack[skip + len(needle) - 1]) - 65]

    return -1