def count_words(s):
    return s.count(' ') + 1


def count_words_v2(s):
    inword = False
    count = 0
    for c in s:
        if c.isalpha() or c.isdigit() or c in '_-':
            if not inword:
                inword = True
                count += 1
        else:
            inword = False

    return count


print(count_words('This is test'))
print(count_words_v2('This   is    test'))