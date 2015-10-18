def disemvowel(comment):
    """Code Wars Problem Text:
    Write a function that takes a string and returns
    a new string with all vowels removed.

    For example, the string "This website is for losers LOL!" would
    become "Ths wbst s fr lsrs LL!".
    """
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    return ''.join([c for c in comment if c.lower() not in vowels])
