class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'*': '*'}  # dictionary that holds our delimiter char

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self.root
        for c in word:
            # if the word is not present, then add it as a new branch
            if c not in curr:
                curr[c] = {}

            # if it is present, then iterate through that dictionary
            curr = curr[c]

        # add the delimiter to mark that word as finished
        curr['*'] = '*'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self.root
        for c in word:
            if c not in curr:
                return False
            curr = curr[c]

        if '*' in curr:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self.root
        for c in prefix:
            if c not in curr:
                return False
            curr = curr[c]
        return True

class Solution:
    # 139. Word Break
    def wordBreak(self, s, wordDict):
        # O(n2*m) time, where n is the length of the string and m the length of the key to search
        trie = Trie()
        # set up the dictionary as a trie
        for word in wordDict:
            trie.insert(word)
        # now validate the actual string
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                # we just want the last string to be valid, that is why we are using the dp bool array
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True
                    break

        # some spaces will be marked as false, they just indicate the places where starting from results in no word
        return dp[-1]





if __name__ == '__main__':
    sol = Solution()
    print(sol.wordBreak("aaaaaaa", ["aaaa","aaa"]))