# Example 1:

# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]

# Output: 5

# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
# return its length 5.


# Example 2:

# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]

# Output: 0

# Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

from string import ascii_lowercase
import copy

class Node:
    def __init__(self, word, path):
        self.word = word
        self.path = path ## this is a list containing word path starting at begin and ending at this word
        

def ladder(begin, end, word_list):
    queue = []

    words = set(word_list)

    queue.append(Node(begin, [begin]))

    while len(queue) > 0:
        cur = queue.pop(0)

        cur_word = cur.word
        path = cur.path

        if cur_word == end:
            print("Final Path:\n")
            return path
            
        ## Search the implied Graph BFS by exploring one character variation at a time
        ## starting from leftmost i=0 all the way to the end character, if you find a match
        ## in the current word list explore it BFS 
        
        print("explore again")
        for i in range(len(cur_word)):
            for c in ascii_lowercase:
                potential_word = cur_word[:i] + c + cur_word[i+1:]

                if potential_word in words:
                    copy_path = copy.deepcopy(path)
                    copy_path.append(potential_word)
                    queue.append(Node(potential_word, copy_path))
                    ## don't need to explore it again so remove it from word list to narrow down the search
                    words.remove(potential_word)
        print([w.path for w in queue])
    return []

print(ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
#print(ladder("hit", "cog", ["hot","dot","dog","lot","log"]))




explore again
[['hit', 'hot']]
explore again
[['hit', 'hot', 'dot'], ['hit', 'hot', 'lot']]
explore again
[['hit', 'hot', 'lot'], ['hit', 'hot', 'dot', 'dog']]
explore again
[['hit', 'hot', 'dot', 'dog'], ['hit', 'hot', 'lot', 'log']]
explore again
[['hit', 'hot', 'lot', 'log'], ['hit', 'hot', 'dot', 'dog', 'cog']]
explore again
[['hit', 'hot', 'dot', 'dog', 'cog']]
Final Path:

['hit', 'hot', 'dot', 'dog', 'cog']











