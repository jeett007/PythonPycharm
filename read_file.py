def read_file(filename):

    try:
        with open(filename, 'r') as file:
            print(f" Reading file content:\n")
            for idx, line in enumerate(file, start=1):
                print(f"Line {idx} : {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


read_file("sample.txt")

