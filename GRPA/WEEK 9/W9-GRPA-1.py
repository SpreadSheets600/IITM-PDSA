def constructWord(word, wordList):
    def backtrack(remaining, path):
        if remaining == '':
            result.append(path.copy())
            return
        for w in wordList:
            if remaining.startswith(w):
                path.append(w)
                backtrack(remaining[len(w) :], path)
                path.pop()

    result = []
    backtrack(word, [])
    return result
