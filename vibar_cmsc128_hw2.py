def getHammingDistance(a,b):
    hd = 0
    if len(a) <= 0 | len(b) <= 0:
        print("Length of any of the strings must not be zero")
    elif len(a) != len(b):
        print("Length of the strings must be equal")
    else:
        for i in range(len(a)):
            if(a[i] != b[i]):
                hd+=1

    return hd
    
def countSubstrPattern(original,pattern):
    occ = 0
    if original.find(pattern,beg=0,end=len(original)) != -1:
        for i in range(len(original)-len(pattern)):
            if original.find(pattern,beg=i,end=len(pattern)) != -1:
                occ+=1
    return occ

def isValidString(string,alphabet):
    for a in alphabet:
        if a not in string:
            return false
    
    return true

def getSkew(string, n):
    gcount = 0
    ccount = 0

    if n <= len(string):
        for i in range(n-1):
            if string[i] == "G":
                gcount+=1                                 
            elif string[i] == "C":
                ccount+=1
                
    return gcount-ccount                 
    
def getMaxSkew(string, n):
    skewlist = []
    skew = 0
    for i in range(n-1):
        skew = getSkew(string,n)
        skewlist.append(skew)
    return max(skewlist)

def getMinSkew(string, n):
    skewlist = []
    skew = 0    
    for i in range(n-1):
        skew = getSkew(string,n)
        skewlist.append(skew)
    return min(skewlist)
    
    
                 
