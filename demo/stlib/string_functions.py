# string functions

MAXLENGTH = 100


def count_upper(s: str) -> int:
    """
    Returns number of uppercase letters in the given string
    :param s: input string
    :return:  count of uppercase letters
    """
    count = 0
    for c in s:
        if c.isupper():
            count += 1

    return count


def hasDigit(s: str) -> bool:
    for c in s:
        if c.isdigit():
            return True

    return False


# Execute only when module is run as script
if __name__ == '__main__':
    print("string_function module")
    print(count_upper("ABc"))
