# Easy: 9
def isPalindrome(x: int) -> bool:
    num = str(x)
    rev_num = num[::-1]

    if num == rev_num:
        return True
    else:
        return False