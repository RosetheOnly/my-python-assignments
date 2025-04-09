# This script reads the content of a file, modifies it, and writes the modified content to a new file.
# It includes error handling for file operations.
# This script reads the content of a file, modifies it, and writes the modified content to a new file.
# It includes error handling for file operations.

def modify_file_content(input_file, output_file):
    """
    Reads the content of a file, modifies it, and writes the modified content to a new file.

    Parameters:
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.
    """
    try:
        # Open the input file for reading
        with open(input_file, 'r') as infile:
            content = infile.readlines()

        # Modify the content (example: convert all text to uppercase)
        modified_content = [line.upper() for line in content]

        # Write the modified content to the output file
        with open(output_file, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Modified content has been written to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file {input_file} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for a valid input file
while True:
    input_file_path = input("Enter the path to the input file: ")
    try:
        with open(input_file_path, 'r') as test_file:
            break  # Exit the loop if the file can be opened
    except FileNotFoundError:
        print(f"Error: The file {input_file_path} does not exist. Please try again.")
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")

# Prompt the user for the output file path
output_file_path = input("Enter the path to the output file: ")

# Call the function to modify the file content
modify_file_content(input_file_path, output_file_path)