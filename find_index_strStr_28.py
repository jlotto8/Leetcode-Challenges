# class Solution:
'''
I: two strings, needle and haystack
O: one int index of the first occurence of needle in haystack
C: 1 <= haystack.length, needle.length <= 104 haystack and needle consist of only lowercase chars
E: needle is not part of haystack
1. I have 2 words, haystack, needle. I need to look at needle and see if it's in haystack
2. If it's in haystack, I go to haystack to where it starts,find the index of that place
2a. If it is not in haystack: return -1
3. I return the index of haystack (where the word needle begins). 
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
Pseudocode:
    for i in range(len(haystack)):
            if needle[0] == haystack[i] #slice?
                found = 
            else:
                return -1
try to go through the string 1 time
use nested for loop
stop comparing when I get to the end of the shorter string
# haystack = "sadbutsad"   needle = "sad"
        '''


# def strStr(self, haystack: str, needle: str) -> int:
    # if needle == haystack:
    #     return 0
    # for i in range(len(haystack)):
    #     for j in range(len(haystack)):
    #         if(haystack[i:j+1]==needle):
    #             print(i)
    #             return(i)
    # return -1
def strStr(haystack,needle):
    # haystack = "sadbutsad"   
    # needle = "sad"
    n = len(needle) #3
    h = len(haystack) #9

    for i in range(h-n + 1):#6 + 1 = 7 if the substring is not identified by the second to last index, and the len of the substring is longer than  the length  of the remaining string: it will not  be there
        match = True
        for j in range(n): #3
            if haystack[i+j] != needle[j]:# haystack i=0 j=0 haystack[i+j] =s +!= s a d
                match = False
                break
        if match:
        # j + 1 == n: # j = index 0,1,2 +1 =3 to match +1 in outer for loop raange
            return(i) # index 
    return(-1)
strStr(haystack = "sadbutsad",needle = "sad" )