def print_formatted(number):
    counter = 1
    width = len(bin(number)[2:])
    while counter <= number:
        num_to_decimal = str(counter).rjust(width)
        num_to_octal = str(oct(counter)).replace('0o', " ").strip().rjust(width)
        num_to_hexadecimal = str(hex(counter)).replace('0x', " ").strip().capitalize().rjust(width)
        num_to_binary = str(bin(counter)).replace('0b', " ").strip().rjust(width)

        print(f"{num_to_decimal} {num_to_octal} {num_to_hexadecimal} {num_to_binary}")
        counter += 1



# print(str(num_to_decimal))
# print(str(num_to_octal))
# print(str(num_to_hexadecimal))
# print(str(num_to_binary))

print_formatted(99)