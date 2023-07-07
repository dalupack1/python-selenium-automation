

def lower_than_average(s):
    lower = []
    amount = 0
    for x in s:
        amount += x
        mean = amount / len(s)
        if x < mean:
            lower.append(x)
    return lower

test_num_1 = [89,42,34,67,81]
print(lower_than_average(test_num_1))


def find_lowest_2(s):
    s.sort()
    return s[:2]
print(find_lowest_2([72,2,1,8,]))