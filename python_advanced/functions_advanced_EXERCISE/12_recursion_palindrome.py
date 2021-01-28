def palindrome(word, index=0, r_index=-1):
    if index == len(word)//2:
        return f'{word} is a palindrome'
    if word[index] == word[r_index]:
        return palindrome(word, index+1, r_index-1)
    else:
        return f'{word} is not a palindrome'
