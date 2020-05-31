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
