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

# Example usage
input_file_path = input("Enter the path to the input file: ")
output_file_path = input("Enter the path to the output file: ")

modify_file_content(input_file_path, output_file_path)