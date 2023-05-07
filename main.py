# Exercise 7

def create_file(filename):
    names = ['Sarah', 'John', 'Amanda', 'Michael', 'Lisa', 'Eric', 'Olivia', 'Derek', 'Emily', 'Joshua']
    with open(filename, 'w') as file:
        file.write('\n'.join(names))
    print(f"File '{filename}' created successfully with {len(names)} names.")


def transform_to_row(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            words = line.split()
            for word in words:
                out_file.write(word + '\n')


def add_greeting(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            out_file.write('Hello ' + line)


def strip_greeting(input_file, output_file):
    with open(input_file, 'r') as in_file, open(output_file, 'w') as out_file:
        for line in in_file:
            out_file.write(line.replace('Hello ', ''))


def combine_files(file1, file2, output_file):
    with open(file1, 'r') as file1, open(file2, 'r') as file2, open(output_file, 'w') as out_file:
        file1_lines = file1.readlines()
        file2_lines = file2.readlines()
        if len(file1_lines) != len(file2_lines):
            print("Error: Files do not have the same number of lines.")
        else:
            for i in range(len(file1_lines)):
                out_file.write(file1_lines[i].strip() + ' ' + file2_lines[i].strip() + '\n')



