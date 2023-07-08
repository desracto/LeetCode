# Easy: 20
def isValid(self, s: str) -> bool:
    """
        The logic behind it is that any paranthesis that's opened must be closed in the same order
        This follows the princple of First In Last Out (FILO) / Last In First Out (LIFO). 
        Meaning the last opened bracket must be the first one to go. 

        We check this by whenever we encounter a closing bracket, check if the top one is the equivalent
        If it is, we remove it

        By the end, if the stack is empty, then the string is valid
    
    """
    convert = {"(": ")", ")": "(", "{": "}", "}": "{", "[": "]", "]": "["}
    stack = []

    for ch in s:
        if ch in ['(', '{', '[']:
            stack.append(ch)
        elif ch in [')', '}', ']']:
            if len(stack) == 0:
                return False
            
            top = stack.pop()
            if top != convert[ch]:
                return False 

    if len(stack) == 0:
        return True 