import re

def find_pattern(text, pattern):
    # Search for the pattern in the text
    match = re.search(pattern, text)
    
    # If a match is found
    if match:
        return match.group()
    return None