# Easy: 12  
def romanToInt(self, s: str) -> int:
    """
        Roman Numeral Pattern is 
        if I before V & X: reduce both by 1
        if X before L & C, reduce both by 10
        if C before D & M, reduce both by 100

        So checking if the current number is lower than the next number, if it is, reduce by that value.
        Add the next one. This will automatically calculate the subtraction for you. 
    """
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    total:int = 0
    for i in range(len(s) - 1):
        if roman[s[i]] < roman[s[i+1]]:
            total -= roman[s[i]]
        else:
            total += roman[s[i]]
    
    return total + roman[s[-1]]