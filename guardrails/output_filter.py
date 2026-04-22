UNSAFE_OUTPUT_KEYWORDS = [
    'hack', 'exploit', 'illegal', 'virus', 'malware', 'crack', 'pirate', 'steal', 'kill', 'harm', 'bomb', 'drug', 'weapon'
]

def filter_output(response_text):
    response_lower = response_text.lower()
    for keyword in UNSAFE_OUTPUT_KEYWORDS:
        if keyword in response_lower:
            return False, f'Contains unsafe keyword: {keyword}'
    return True, ''