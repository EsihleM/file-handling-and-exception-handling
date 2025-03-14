def read_and_modify_file():
    input_filename = input("Enter the filename to read: ")
    output_filename = "modified_" + input_filename

    try:
        with open(input_filename, 'r') as file:
            data = file.read()
           
            modified_data = data.upper()

        with open(output_filename, 'w') as new_file:
            new_file.write(modified_data)
        print(f"Modified file has been saved as {output_filename}.")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except IOError:
        print("Error: The file can't be read.")

read_and_modify_file()
