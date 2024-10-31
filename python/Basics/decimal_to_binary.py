def decimal_to_binary(number):
    if number >= 0 and number <= 255:
        return bin(number)[2:]

    return 'The number is not in range (0 - 255)'

print(decimal_to_binary(0))
print(decimal_to_binary(192))
print(decimal_to_binary(2323))
