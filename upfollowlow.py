#Problem Statement - Given a string of sixe N. In one move you can change the 
#case of the character(i.e form lower case to upper case and vice versa).
#You need to find the minimum number of moves such that zero or more upper 
#case characters are followed by zero or more lower case characters.
#constraints: 1 <= N <=10^5, 1 <= len(str) <=10^5.
def solve(N, str):
    import re
    pat = '^[A-Z+]+[a-z]+$'
    uc = 0
    lc = 0
    if str.isupper():
        return 0
    elif str.islower():
        return 0
    elif re.search(pat, str):
        return 0
    else:
        for x in str:
            if x.isupper():
                uc+=1
            else:
                lc+=1
        return(min(uc,lc))

n = 5
a = 'abcDEFG'
print(solve(n, a))
