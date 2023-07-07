def split_str(s):
    length = len(s)
    half = length // 2
    add = 0
    if length % 2:
        add = 1
    left = s[:half + add]
    right = s[half + add:]
    return right + left

test_string_1 = 'aaabbbbcc'
test_string_2 = 'acbb'
print(split_str(test_string_1))
print(split_str(test_string_2))



def unique_chars(s):
    lenstr = len(s)
    lenset = len(set(s))
    return lenstr == lenset

test_char_1 = 'abcdef'
test_char_2 = 'aabcde'
print(unique_chars(test_char_1))
print(unique_chars(test_char_2))