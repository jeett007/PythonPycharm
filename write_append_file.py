def write_and_append():
    filename = "output.txt"

    data = input("Enter some data to write to the file: ")
    with open(filename, 'w') as file:
        file.write(data + "\n")

    more_data = input("Enter additional data to append: ")
    with open(filename, 'a') as file:
        file.write(more_data + "\n")

    print("\nFinal content of the file:")
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())


write_and_append()
