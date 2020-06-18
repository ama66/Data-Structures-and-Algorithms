# Welcome to Facebook!

# This is just a simple shared plaintext pad, with no execution capabilities.

# When you know what language you would like to use for your interview,
# simply choose it from the dropdown in the top bar.

# Enjoy your interview!




1, Merge a list of intervals

Given a list of intervals (a pair of start and end timestamp), return a list of merged intervals


Input: [[2, 6], [1, 3],  [7,8]]
Output:  [[1,6], [7,8]]
    
Input.sort(key= lambda x: x[0])
## 


Output=[[[1, 3], [2, 6],  [7,8]]]

if len(Input)>0:
    start, end = Input[0] 
else:
    return Input 

for inv in Input[1:]:
    cur_st,cur_end = inv 
    if cur_st <= end:
        ## merging case
        end = max(end, cur_end) 
    else:
        Output.append([start,end])
        start=cur_st
        end =cur_end 

Output.append([start,end])

return Output 

## [[1,6],[7,8]]

Input: [[2, 6], [1, 3],  [6,8]]
Output:  [[1,8]]
    
#########

##

## Two pointers 

    
2, Merge Two Sorted Interval Arrays

Consider the concept two sorted,non overlapping interval lists
Given two of these interval lists, return a 3rd interval list that is the union of the input interval lists. 

Can assume all positive integers. Feel free to design data structures.

For example:

Input:

L1 [[1,2], [3,9]]

L2 [[4,6], [8,10], [11,12]]

   [3 .     9]
     [4 6] [8 10]
        
  [3          10]

Output should be:

[[1,2], [3,10], [11,12]]


start1=0
start2=0






