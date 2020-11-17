# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:

even_numbers = []
for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
print(even_numbers)
# 2. Print the difference between the largest and smallest value:

numbers.sort()
print(numbers[-1] - numbers[0])
# 3. Print True if the list contains a 2 next to a 2 somewhere.
numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]
double_2 = 0
for number in numbers:
    if number == 2:
        double_2 += 1
        if double_2 == 2:
            print(True)
    else:
        double_2 = 0
# 4. Print the sum of the numbers, 

#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
numbers_total = 0
turn_off_count = 0
for number in numbers:
    if number == 6:
        turn_off_count = 1
    if turn_off_count == 0:
        numbers_total += number
    if number == 7:
        turn_off_count = 0
    
    
print(numbers_total)

# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 







