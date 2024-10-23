word = input('type a word: ')

if word.lower() == word[::-1].lower():
    print('palindrome')
else:
    print('non palindrome')