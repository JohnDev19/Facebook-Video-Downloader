import re

def sanitize_title(title):
    """Sanitize the title to create a valid filename."""
    return "".join([c for c in title if c.isalpha() or c.isdigit() or c in (' ', '-', '_')]).rstrip()
