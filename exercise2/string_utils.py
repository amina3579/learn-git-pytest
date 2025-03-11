# Exercise 2: String Utilities


def reverse_string(s: str) -> str:
    """
    Return the input string in reverse order.

    Args:
        s: Input string

    Returns:
        The reversed string
    """
    # TODO: Implement this function
    return ( s[::-1])
    pass
reverse_string("abracadabra")
    pass


def count_vowels(s: str) -> int:
    """
    Return the number of vowels (a, e, i, o, u) in the input string.
    Case-insensitive: both uppercase and lowercase vowels should be counted.

    Args:
        s: Input string

    Returns:
        The number of vowels in the string
    """
    # TODO: Implement this function
    L=list(s)
    Vowels=['a', 'e', 'i', 'o', 'u']
    count = 0
    for i in range (len(L)) :
        if L[i].lower() in Vowels:
            count+=1
    return count
count_vowels('flagadouille')

    pass


def is_palindrome(s: str) -> bool:
    """
    Check if the input string is a palindrome.
    A palindrome reads the same backward as forward.
    Spaces and case should be ignored.

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """
    # TODO: Implement this function
    return ( s==s[::-1])
    pass
is_palindrome("madam")



def capitalize_words(s: str) -> str:
    """
    Capitalize the first letter of each word in the input string.

    Args:
        s: Input string

    Returns:
        The input string with the first letter of each word capitalized
    """
    # TODO: Implement this function
    if not s:  # handle empty string
        return ""
    return s[0].upper() + s[1:].lower()
    pass
capitalize_words("marmite")
    pass
