#--------------------- Permutation ----------------------
def toString(List):
    return ''.join(List)

def permute(a, l, r):
    if l==r:
        print toString(a)
    else:
        for i in xrange(l,r+1):
            a[l], a[i] = a[i], a[l]
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l] # backtrack
 
# Driver program to test the above function
'''
string = "ABCD"
n = len(string)
a = list(string)
permute(a, 0, n-1)
'''

#---------------- Find permutation ---------------------
def findPermutationInString(sStr, bStr):
    M = len(sStr)
    N = len(bStr)
    sSharCount = [0] * 256 #There are total 256 characters in ACSII
    bSharCount = [0] * 256
    for i in xrange(0, M):
        sSharCount[ord(sStr[i])] += 1
        bSharCount[ord(bStr[i])] += 1
        
    for i in xrange(M, N):
        if sSharCount == bSharCount:
            print('Found permutation at index ' + str(i-M))
            
        # Move to next window
        # - add next char
        bSharCount[ord(bStr[i])] += 1      
        # - remove first char
        bSharCount[ord(bStr[i-M])] -= 1
        
    # Compare for the last window
    if sSharCount == bSharCount:
        print('Found permutation at index ' + str(N-M))    
         
#findPermutationInString('ABCD', "BACDGABCDA")


#--------- Find sub string ------------------------------
from DataStructureHashTable import MyHashTable

def findSubString(sStr, bStr):
    sHash = MyHashTable.getHash(sStr)
    sLen = len(sStr)
    bLen = len(bStr)
    bHashs = [None] * ( bLen- sLen + 1)
    for i in range(0, bLen - sLen + 1):
        if i == 0:            
            bHashs[i] = MyHashTable.getHash(bStr[i:i+sLen])
        else:           
            bHashs[i] = ((bHashs[i-1] - ord(bStr[i-1:i]) * 128**(sLen-1)) * 128 + ord(bStr[i+sLen-1:i+sLen])) % MyHashTable.SIZE
        if bHashs[i] == sHash:
            if sStr == bStr[i:i+sLen]:
                return i
    return -1    


#print(findSubString('doe', 'you are seeing doe s book'))


def duplicateIndex(str):
    stack = []
    for i in range(0, len(str)):
        if len(stack) > 0 and stack.pop() == str[i]:
            return i-1
        else:
            stack.append(str[i])        
    return -1        
            
   
# Aware of unpacking. cannot use a, b = (c,d)     
def super_reduced_string(s):   
    dupIdx = duplicateIndex(s)    
    if dupIdx == -1:
        return (s if s else 'Empty String')
    else:
        newStr = s[:dupIdx] + s[dupIdx+2:]
        return super_reduced_string(newStr)

print(super_reduced_string('aaabccddd')) 
print(super_reduced_string('aaaa'))
print(super_reduced_string('aabbaa'))
print(super_reduced_string('abcdefg'))
print(super_reduced_string(''))