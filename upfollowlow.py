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