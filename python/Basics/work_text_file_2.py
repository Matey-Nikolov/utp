def text_file_operation(path_to_input_file, path_to_output_file):
    file_input = open(path_to_input_file, 'rt')

    filtered_lines = []

    for one_line in file_input:
        if one_line.strip() and not one_line.strip().startswith('#'):
            filtered_lines.append(one_line)


    file_input.close()

    # print(filtered_lines)

    file_output = open(path_to_output_file, 'w')
    file_output.writelines(filtered_lines)
    file_output.close()

text_file_operation('input_data_2.txt', 'output_file.txt')