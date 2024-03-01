def escape_special_characters(char):
    if ord(char) < 32 or char == '\\' or char == '\n' or char == '"':
        return '\\{:03o}'.format(ord(char))
    else:
        return char

with open("sample-data.txt", "r") as input_file:
    values = [float(line.strip()) for line in input_file if line.strip()]

converted_values = [escape_special_characters(chr(int((value + 1) * 127))) for value in values]
result_string = "".join(converted_values)

with open("compressed-hq.txt", "w") as output_file:
    output_file.write(result_string)

print(result_string.strip()) # for xcopy

