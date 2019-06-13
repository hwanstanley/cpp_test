def is_palindrome(word):
    word = word.lower()
    n = len(word)
    return all(word[i] == word[n-i-1] for i in range(round(n/2)))
    
print(is_palindrome('Deleveled'))