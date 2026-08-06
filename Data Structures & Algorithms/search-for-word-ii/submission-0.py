class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


class Solution:
    def buildTrie(self, words):
        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.word = word
        return root

    def backtrack(self, i, j, parent):
        letter = self.board[i][j]
        curr_node = parent.children[letter]

        if curr_node.word:
            self.result.append(curr_node.word)
            curr_node.word = None  # avoid duplicates

        self.board[i][j] = "#"  # mark visited

        for x, y in [(0,1), (1,0), (0,-1), (-1,0)]:
            ni, nj = i + x, j + y
            if 0 <= ni < len(self.board) and 0 <= nj < len(self.board[0]) and self.board[ni][nj] in curr_node.children:
                self.backtrack(ni, nj, curr_node)

        self.board[i][j] = letter  # restore

        if not curr_node.children:
            parent.children.pop(letter)

    def findWords(self, board, words):
        self.board = board
        self.result = []
        root = self.buildTrie(words)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] in root.children:
                    self.backtrack(i, j, root)

        return self.result
