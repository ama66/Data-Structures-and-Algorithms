# (7)
# HTTPRouter using a Trie For this exercise we are going to implement an HTTPRouter like you would find in a typical web server using the Trie data structure we learned previously.

# There are many different implementations of HTTP Routers such as regular expressions or simple string matching, but the Trie is an excellent and very efficient data structure for this purpose.

# The purpose of an HTTP Router is to take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content to return. In a dynamic web server, the content will often come from a block of code called a handler.

# Bonus Points: Add a not found handler to your Router which is returned whenever a path is not found in the Trie.

# More Bonus Points: Handle trailing slashes! A request for '/about' or '/about/' are probably looking for the same page. Requests for '' or '/' are probably looking for the root handler. Handle these edge cases in your Router.

# =
# 1


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self,root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root=RouteTrieNode('/',root_handler)

    def insert(self, path,path_handler):
        ## Path is a list of words obtained by splitting the URL on "/"
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        ## Add a word to the Trie
        
        node = self.root
        for word in path:
            if word not in node.children:
                node.insert(word) 
            # Recurse! 
            node=node.children[word]   
        ## Add handler to last node    
        node.handler = path_handler      
   
    def find(self, path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if path==["/"]:
            return self.root.handler 
        
        node = self.root
        ## Empty trie case
        if not node.children:
            return False 
        for word in path:
            flag=False
            for child in node.children:
                if  node.children[child].word == word:
                    node = node.children[child]
                    flag=True
                    break ## ends first for loop but not the second 
                    
            # if we loop over all children and cannot find a word
            ## we simply return False 
            if not flag:
                return None 
        ## if we are here without return, then 
        ## all words were found and node is the last word of path...return its handler
        return node.handler
        
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self,word,handler=None):
        ## Initialize this node in the Trie
        self.word = word ## word/part of the path obtained by website.split(“/”)
        self.children = {} ## hashset of all children 
        self.handler = handler ## Handler with None as default value
        
    def insert(self, new_word):
        ## Add a child node in this Trie
        self.children[new_word]=RouteTrieNode(new_word)




# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self,root_handler,notfound_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.trie=RouteTrie(root_handler)
        self.notfound_handler=notfound_handler

    
    def add_handler(self,url,handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        self.trie.insert(self.split_path(url),handler)
        
    
    def lookup(self,url):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        h=self.trie.find(self.split_path(url))
        return h if h else self.notfound_handler

    def split_path(self,url):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [x for x in url.split("/") if x != ''] if url!="/" else ["/"]
       


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler") # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/")) # should print 'root handler'
print(router.lookup("/home")) # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about")) # should print 'about handler'
print(router.lookup("/home/about/")) # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me")) # should print 'not found handler' or None if you did not implement one


