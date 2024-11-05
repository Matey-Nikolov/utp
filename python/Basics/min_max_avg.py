def max_value(numbers_list):

    max = numbers_list[0]
    for i in numbers_list:

        if i > max:
            max = i

    return max

def min_value(numbers_list):
    min = numbers_list[0]
    for i in numbers_list:

        if i < min:
            min = i

    return min


def find_min_max_avg(numbers_list):
    max = max_value(numbers_list)
    minimum = min_value(numbers_list)

    average = 0
    for x in numbers_list:
        average = average + abs(x)

    average = average / len(numbers_list)

    return 'Max value: {}, minimum  value {}, average value {}.'.format(max, minimum, average)

list_numbers = [0, 9, -3, 243, 11, -100]
print(find_min_max_avg(list_numbers))