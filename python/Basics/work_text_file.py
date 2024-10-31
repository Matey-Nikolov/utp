def text_file_operation(path_to_file):
    list_numbers_final = []

    file_numbers = open(path_to_file, 'rt')

    for one_line in file_numbers:
        #Convert string list to numbers list
        numbers = [int(number) for number in one_line.split()]

        list_numbers_final.append(min(numbers))

    file_numbers.close()

    print(list_numbers_final)

text_file_operation('input_data.txt')