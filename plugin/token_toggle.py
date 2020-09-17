token_pairs = {
        'true': 'false',
        'false': 'true',
        'yes': 'no',
        'no': 'yes',
        '1': '0',
        '0': '1',
        'on': 'off',
        'off': 'on',
        '==': '!=',
        '!=': '==',
        '>': '<=',
        '<=': '>',
        '<': '>=',
        '>=': '<',
        '+': '-',
        '-': '+',
        '*': '/',
        '/': '*',
        }

def format_token(word, toggled_word):
    if word.isupper():
        toggled_word = toggled_word.upper()
    elif word.istitle():
        toggled_word = toggled_word.title()
    return toggled_word

def token_toggle(word):
    toggled_word = word
    try:
        toggled_word = token_pairs[word.lower()]
        toggled_word = format_token(word, toggled_word)
    except:
        print('Uncovered token. Maybe you want to add it to the list.')
    return toggled_word
