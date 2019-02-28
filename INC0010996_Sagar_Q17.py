def palindromesubsequence(x,y):
    m = len(x)
    n = len(y)
    L = [[0]* (n+1)]*(m+1)
    for i in range(n+1):
        for j in range(n+1):
            if (i==0 or j==0):
                L[i][j]=0;
            elif (x[i-1] == y[j-1]):
                L[i][j] = L [i-1][j-1]+1;
            else:
                pass
            
        return L[0] [n-1]
    
            
def longestpalindromesubsequence(ABCCBDDCE):  
    return (string)
