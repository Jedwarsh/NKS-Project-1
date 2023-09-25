# Open the file for reading and return the values in an array
def read_words(file_name):
    with open(file_name, 'r') as file:

        lines = []
        for line in file:
            lines.append(line.strip())

        return lines

# Open a file and check if a string exists in it or not
def string_exists_in_file(filename, search_string):
    try:
        with open(filename, 'r') as file:
            for line in file:
                if search_string in line:
                    return True  # String found in at least one line
        return False  # String not found in any line
    except FileNotFoundError:
        return False  # File not found

