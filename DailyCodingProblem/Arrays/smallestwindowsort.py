L=[1,2,3,4,5,8,10,9,12,6,7,13,14,15]
## Smallest window for sorting here to be sorted is [8,10,9,12,6,7] so left=5 and right = 10
## First Solution
#1) sort the array and call it s
## find first and last indices where original array is not same as sorted

def windowsort(L):
    left,right = None, None
    s = sorted(L)
    for i in range(len(L)):
        if L[i]!=s[i] and left==None:
            left=i  # first time this happens left will be set to and index and the condition won't be satisfied again
        elif L[i]!=s[i]: ## This will keep moving through the middle window until right is set to the last element index
            right=i
    return left, right
## This algorithm is O(nlog(n)) since it is dominated by sorted(L) which takes O(nlogn) in space and time
print("O(nlogn) Algorithm based on sorted array")
print(L)
left,right= windowsort(L)
print(left, right)

#### Second Solution relies on keeping track of increasing index (current max) as we traverse from left to right the array
### how? keep track of maximum seen so far until you hit the unsorted window to find numbers that are smaller
### Than the current max , keep moving by setting the right bound to such small numbers until you hit last one
## Also traverse from right to left keeping track of decreasing indices (current minimum) until you hit the unsorted
# window to find numbers bigger than the current minimum...keep setting these numbers to the left bound until you hit
## the true left bound. All subsequent numbers will be smaller than current minimum which keeps moving till beginning
##  of the array

# This is O(n) in time and O(1) in space (only need to store left, right, max_seen, min_seen vars)
def windowsortrack(L):
    left, right = None, None
    n=len(L)
    max_seen,min_seen= -float("inf"), float("inf") # Max rep numbers to initialize vars

    # Left traversal tracking max and right boundary
    for i in range(n):
        max_seen=max(max_seen,L[i])
        if L[i] < max_seen:
            right = i

    # Left traversal tracking max and right boundary
    for i in range(n-1,-1,-1):  # Reverse list
        min_seen = min(min_seen, L[i])
        if L[i] > min_seen:
            left = i
    return left, right

print("O(n) , O(1) time and space Algorithm based on tracking left and right boundaries")
print(L)
left,right= windowsortrack(L)
print(left, right)







