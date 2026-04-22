UNSAFE_KEYWORDS = [
    'hack', 'exploit', 'illegal', 'virus', 'malware', 'crack', 'pirate', 'steal', 'kill', 'harm', 'bomb', 'drug', 'weapon'
]

def filter_input(user_input):
    user_input_lower = user_input.lower()
    for keyword in UNSAFE_KEYWORDS:
        if keyword in user_input_lower:
            return False, f'Contains unsafe keyword: {keyword}'
    return True, ''