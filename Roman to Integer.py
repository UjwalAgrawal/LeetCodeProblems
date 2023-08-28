s = 'XLIX'
d = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
total = 0
for i in range(1,len(s)):
    if(d[s[i-1]] >= d[s[i]]):
        total+=d[s[i-1]]
    else:
        total +=  - d[s[i-1]]
        
        
print(total + d[s[-1]])

#('XLIX') 49
#('MCMXCIV') 1994