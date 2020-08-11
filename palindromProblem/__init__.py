def palindrom(word):
    if not word: return False
    
    return word == word[::-1]