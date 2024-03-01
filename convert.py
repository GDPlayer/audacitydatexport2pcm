with open("sample-data.txt", "r") as input_file:
    values = [float(line.strip()) for line in input_file if line.strip()]

converted_values = [chr(int((value + 1) * 37 + 48)).replace('\\', '\\\\').replace('\n', '\\n') for value in values]

with open("compressed-sample-data.txt", "w") as output_file:
    output_file.write("".join(converted_values))

