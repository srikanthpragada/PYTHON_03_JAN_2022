# string functions

def count_upper(s):
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def hasDigit(s):
    for c in s:
        if c.isdigit():
            return True

    return False
