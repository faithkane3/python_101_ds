# python_101_ds
This is code from my pre-work assignment for Codeup.
This is code I wrote to practice basic Python skills before starting Codeup, 
and I'm posting it here as a baseline for my data science program.

def has_vowels(string):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    for char in string:
        if char in vowels:
            return True
    return False

def count_vowels(string):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    count = 0
    for char in string:
        if char in vowels:
            count = count + 1
    return count
    
def remove_vowels(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
    for char in vowels:
        text = text.replace(char, '')
    return text
    
def starts_with_vowel(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
    return text.startswith(vowels)
    
def ends_with_vowel(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
    return text.endswith(vowels)
    
