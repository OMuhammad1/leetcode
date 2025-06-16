class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        visited = set()
        wordSet = set(wordList)

        if endWord not in wordList:
            return 0

        q.append((beginWord, 1))
        visited.add(beginWord)

        def newChar(word, depth): 
            for i in range(len(word)):
                for char in string.ascii_lowercase:
                    tempWord = word[:i] + char + word[i+1:]
                    if tempWord in wordSet and tempWord not in visited:
                        visited.add(tempWord)
                        q.append((tempWord, depth + 1))

        while q:
            word, depth = q.popleft()
            if word == endWord:
                return depth
            newChar(word, depth)
        
        return 0