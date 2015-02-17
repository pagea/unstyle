"""Module containing character feature extractors."""

import string
from stylproj.features.featregister import register_feat

@register_feat
def characterSpace(text):
    """Return the total number of characters."""
    return len(text)

@register_feat
def letterSpace(text):
    """Return the total number of letters (excludes spaces and punctuation)"""

    count = 0;
    alphabet = string.ascii_lowercase + string.ascii_uppercase
    for char in text:
        if char in alphabet:
            count += 1
    return count
