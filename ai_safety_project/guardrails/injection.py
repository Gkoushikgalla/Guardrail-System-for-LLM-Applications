INJECTION_PATTERNS = [
    'ignore previous instructions',
    'ignore all previous',
    'you are now',
    'act as',
    'role-play as',
    'pretend to be',
    'break character',
    'override',
    'system prompt',
    'jailbreak'
]

def detect_injection(user_input):
    user_input_lower = user_input.lower()
    for pattern in INJECTION_PATTERNS:
        if pattern in user_input_lower:
            return False, f'Potential prompt injection: {pattern}'
    return True, ''