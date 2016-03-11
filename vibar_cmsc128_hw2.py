#=================================#
#   Aron John S. Vibar            #
#   2013-03369 CMSC 128 AB-1L     #
#   2nd Programming Assignment    #
#=================================#

#Returns the "Hamming Distance" of two strings of the same length
def getHammingDistance(a,b):
    hd = 0 #hamming distance
    if len(a) <= 0 | len(b) <= 0:
        print("Length of any of the strings must not be zero")
    elif len(a) != len(b):
        print("Length of the strings must be equal")
    else:
        for i in range(len(a)):
            if(a[i] != b[i]):
                hd+=1

    return hd
    
#Returns the number of occurences of a given pattern in a given string
def countSubstrPattern(original,pattern):
    occ = 0 #number of occurence
    if original.find(pattern,0,len(original)) != -1:
        for i in range(len(original)-len(pattern)+1):
            if original.find(pattern,i,len(pattern)+i) != -1:    
                occ+=1
    return occ

#Returns true if all chars of the string uses the given alphabet,false otherwise
def isValidString(string,alphabet):
    for a in string:
        if a not in alphabet:
            return False
    
    return True

#Returns the # of skews from the 1st element of the string to the nth element
def getSkew(string, n):
    gcount = 0 #number of G's encountered
    ccount = 0 #number of C's encountered
    skew = 0
    if n < len(string):
        for i in range(n):
            if string[i] == "G":
                gcount+=1                                 
            elif string[i] == "C":
                ccount+=1
    skew = gcount-ccount            
    return skew
            
#Returns the max. skews from the 1st element of the string to each nth element
def getMaxSkew(string, n):
    skewlist = [] #list of the number of skews from 1 to each n
    if len(string) <= 0:
        return 0
    else:
        for i in range(n):
            skewlist.append(getSkew(string,i+1))
            return max(skewlist)

#Returns the min. skews from the 1st element of the string to each nth element
def getMinSkew(string, n):
    skewlist = []
    if len(string) <= 0:
        return 0
    else:
        for i in range(n):
            skewlist.append(getSkew(string,i+1))
        return min(skewlist)    
    
