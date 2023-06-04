# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

number = 5
x = 0
for num in range(number):
     num = num + 1
     x += num
print(x)


# Find the max number from 3 values.
# Example: 124, 21, 32. Result = 124.

num_1 = 21
num_2 = 32
num_3 = 124
if num_1 > num_2 and num_3: print(num_1)
if num_2 > num_3 and num_1: print(num_2)
if num_3 > num_1 and num_2: print(num_3)

# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).



def odd_even_digit_count(n):
    odds = 0
    evens = 0

    while n != 0:
        current_digit = n %10
        if current_digit %2:
            evens += 1
        else:
            odds += 1
        n = n//10

    print(f'Evens {evens}, Odds {odds}')

example_number = 34571

odd_even_digit_count(example_number)