## Word Concatenation

class Solution(object):
  def findAllConcatenatedWords(self, words):
    ## For constant time look up
    wordDict = set(words)
    cache = {} ## memoize in case you saw that word before no need to check if it can be broken down 
    ## into words we have seen in the list of words
    return [word for word in words if self._canForm(word, wordDict, cache)]

  def _canForm(self, word, wordDict, cache):
    ## if the subword could be broken down into words contained in the dictionary (prefix + suffix)
    ## then return true
    
    if word in cache:
      return cache[word]

    for index in range(1, len(word)):
      ## try all starting indexes and break down the word into two parts a prefix and a suffix
    ## and check if both are contained in a dictionary. in case of a suffix check recursively as well
    ##  and update the hashmap to avoid repeated calculations
    
      prefix = word[:index]
      suffix = word[index:]
    
      if prefix in wordDict:
        if suffix in wordDict or self._canForm(suffix, wordDict, cache):
          cache[word] = True
          return True
    ## If I came out of this loop without returning then the word cannot possibly be broken down 
    ## into words that exist in the list so update the cache and return false 
    
    cache[word] = False
    return False

input = ['cat', 'cats', 'dog', 'catsdog']

print(Solution().findAllConcatenatedWords(input))
## ['catsdog']

### Median of a stream of numbers 

## import heapq
## Note that we do not have maxheap 
## so to use minheap we multiply numbers by -1 for example if 7 is max element then -7 is minelement! 

def get_median(min_heap, max_heap):
  if len(min_heap) > len(max_heap):
    return min_heap[0]
  elif len(min_heap) < len(max_heap):
    return -max_heap[0]

  else:
    min_root = min_heap[0]
    max_root = -max_heap[0]
    return (min_root + max_root) / 2.0



def add(num, min_heap, max_heap):
  if len(min_heap) + len(max_heap) <= 1: # if one is empty add to the maxheap 
    heapq.heappush(max_heap, -num)
    return

  median = get_median(min_heap, max_heap)
    
  if num > median:
    heapq.heappush(min_heap, num)
  else:
    heapq.heappush(max_heap, -num)

def rebalance(min_heap, max_heap):
  if len(min_heap) > len(max_heap) + 1:
    root = heapq.heappop(min_heap)
    heapq.heappush(max_heap, -root)
    
  elif len(max_heap) > len(min_heap) + 1:
    root = -heapq.heappop(max_heap)
    heapq.heappush(min_heap, root)

def print_median(min_heap, max_heap):
  print(get_median(min_heap, max_heap))

def running_median(stream):
 ## initialize two heaps for the elements below the median (maxheap)  and above the median (minheap)
  min_heap = []
  max_heap = []
  ### Algorithm
  for num in stream:
    #(1) add to min or maxheap
    add(num, min_heap, max_heap)
    #(2)rebalance heaps if one is > the other by 2 numbers 
    rebalance(min_heap, max_heap)
    ## (3) compute and print median 
    print_median(min_heap, max_heap)

running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2



# Merge K Sorted Linked Lists
# Coding Sessions

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ''
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer


def merge(lists):
  arr = []
  for node in lists:
    while node:
      arr.append(node.val)
      node = node.next
  head = root = None
  for val in sorted(arr):
    if not root:
      head = root = Node(val)
    else:
      root.next = Node(val)
      root = root.next
  return head


def merge2(lists):
## Create dummy headnode for the merged linked list

  head = current = Node(-1)

  while any(list is not None for list in lists):
    current_min, i = min((list.val, i)
                         for i, list in enumerate(lists) if list is not None)
    lists[i] = lists[i].next
    current.next = Node(current_min)
    current = current.next

  return head.next


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))

print(a)
# 135
print(b)
# 246
print(merge2([a, b]))
# 123456


######## Bruteforce 

from __future__ import print_function
from heapq import *


class ListNode:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def merge_lists(lists):
  ## Bruteforce
    elems=[]

    for l in lists:
        resultHead = l
        while resultHead:
            elems.append(resultHead.value)
            resultHead=resultHead.next
    elems.sort()
    
    idx=0
    while idx < len(elems):
        if idx==0:
            head=ListNode(elems[idx])
            cur=head
            idx+=1 
        else:
            cur.next=ListNode(elems[idx])
            cur=cur.next 
            idx+=1 
            
    # TODO: Write your code here
    return head


def main():
  # l1 = ListNode(2)
  # l1.next = ListNode(6)
  # l1.next.next = ListNode(8)
  l1=ListNode(2,ListNode(6,ListNode(8)))
  # l2 = ListNode(3)
  # l2.next = ListNode(6)
  # l2.next.next = ListNode(7)
  l2=ListNode(3,ListNode(6,ListNode(7)))
  # l3 = ListNode(1)
  # l3.next = ListNode(3)
  # l3.next.next = ListNode(4)
  l3=ListNode(1,ListNode(3,ListNode(4)))

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next


main()

