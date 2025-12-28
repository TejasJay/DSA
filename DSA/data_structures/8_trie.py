# This is a tree Data structure called trie or prefix tree because we solve the problems related to word prefixes useful for auto completion

class Node:
    def __init__(self):
        self.children = dict() 
        self.is_end_of_word = False # this determines if we reached the end of the word 

class Trie:
    def __init__(self):
        self.root = Node() # every trie has a root node with a empty child dictionary and is not the end of the word by default

    # O(m) - where m is the lenght of the word
    def insert(self, word): # inserts a new word into the trie
        current_node = self.root # we point from the root
        for c in word: 
            if c not in current_node.children: # we check if this character is not part of the current node's children's dictionary's key
                current_node.children[c] = Node() # if its not a part then we create a node at that point or index
            current_node = current_node.children[c] # we move forward to the next node irrespective of if we created a new node or not
        current_node.is_end_of_word = True # we set the end of the word to True after we reach the last character in the word

    # O(m) - where m is the lenght of the word
    def search(self, word): # searches if a word is part of a trie
        current_node = self.root # we point from the root
        for c in word: 
            if c not in current_node.children: # we check if this character is not part of the current node's children's dictionary's key
                return False # because the character isnt in the children dictionary, which means the word does not exist
            current_node = current_node.children[c] # if the character is present from the previous step, then we move the pointer to the next node/character and check the character
        return current_node.is_end_of_word # once we reach the end of the word its last charcter is set to True because it is the end of that word, hence we will return True

    # O(m) - where m is the lenght of the word
    def delete(self, word):
        self._delete(self.root, word, 0) # says I want to delete the word and Im currently at the root node and I am at index 0 of the word

    # O(m) - where m is the lenght of the word
    def has_prefix(self, prefix): # to check if the prefix is part of a word as a part of the trie
        current_node = self.root # we point from the root
        for c in prefix: 
            if c not in current_node.children: # we check if this character is not part of the current node's children's dictionary's key
                return False # because the character isnt in the children dictionary, which means the word does not exist
            current_node = current_node.children[c] # if the character is present from the previous step, then we move the pointer to the next node/character and check the character
        return True # to check the prefix we just return True because it doesnt have to be end of the word such as the search function, we are just looking to see if the prefix of the word actually exists in the trie

    # O(m + k) - where m is the lenght of the prefix and k is the total number of characters in all suffixes
    def starts_with(self, prefix): # returns all the words that starts with the prefix
        words = []
        current_node = self.root # this is the pointer and we start at the root node
        for c in prefix:
            if c not in current_node.children: # if there are no children then return empty list
                return words 
            current_node = current_node.children[c] # if the node does exist then move there, till the last point of the prefix and from this point, do a depth first search
        def _dfs(current_node, path): # a sub method to do a DFS
            if current_node.is_end_of_word: # we want to append to the words list
                words.append(''.join(path)) # we get all the characters, join them and then append them to the words list
            for c, child_node in current_node.children.items(): # c is the character that performs the transition, child_node is the node that the transition is performed to
                _dfs(child_node, path + [c]) # we do a recurssive call by extending the character list
        _dfs(current_node, list(prefix))
        return words

    # O(n) - number of nodes in the Trie
    def list_words(self): # returns all the words
        words = []
        def _dfs(current_node, path): # a sub method to do a DFS
            if current_node.is_end_of_word: # we want to append to the words list
                words.append(''.join(path)) # we get all the characters, join them and then append them to the words list
            for c, child_node in current_node.children.items(): # c is the character that performs the transition, child_node is the node that the transition is performed to
                _dfs(child_node, path + [c]) # we do a recurssive call by extending the character list
        _dfs(self.root, [])
        return words


    def _delete(self, current_node, word, index):
        if index == len(word): # this is the terminating case to determine we have processed all the characters in the word
            if not current_node.is_end_of_word: # checking if the current node is not the end of the word
                return False # we return False because we dont have to delete anything because the word we want to delete doesnt exist
            current_node.is_end_of_word = False # if the above condition doesnt meet then that means it is the end of of the word, but now we explicitly set it to False to says this is no longer a word.
            return len(current_node.children) == 0 # this return True if the current node doesnt have child nodes, if it doesnt have child nodes its safe to delete, but if it does then we need to handle that.
        c = word[index] # if the above condition returns False, then we set that the current character is in the word at the index
        node = current_node.children.get(c) # from the current node we get the children for that character in 'c'
        if node is None: # there is a possibility that there might be no children
            return False # because the word doesnt exist
        delete_current_node = self._delete(node, word, index+1) # now we recurssively delete for every charcater / node in the word if True is returned by the previous step. This is going to return either a True or False.
        if delete_current_node: # if delete_current_node returns True, then we proceed further
            del current_node.children[c] # now we can delete the character or the node 
            return len(current_node.children) == 0 and not current_node.is_end_of_word # delete if it has no children and is not the end of the word
        return False 


if __name__ == "__main__":
    trie = Trie()

    trie.insert("hello")
    trie.insert("henry")
    trie.insert("mike")
    trie.insert("minimal")
    trie.insert("minimum")

    print(trie.list_words())

    print(trie.has_prefix("mi"))

    print(trie.starts_with("mi"))

    trie.delete("minimal")

    print(trie.starts_with("mi"))

    print(trie.search("minimum"))
    print(trie.search("minimal"))
    print(trie.search("mini"))

    trie.insert("mini")

    print(trie.starts_with("mi"))
