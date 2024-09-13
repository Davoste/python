
# file_handling_assignment.py

def create_file():
    try:
        # Creating a new text file in write mode
        with open("my_file.txt", 'w') as file:
            file.write("Hello, this is the first line.\n")
            file.write("This is the second line with a number: 123.\n")
            file.write("Third line here!\n")
        print("File created and text written successfully.")
    except Exception as e:
        print(f"An error occurred during file creation: {e}")
    finally:
        print("File creation operation complete.")

def read_file():
    try:
        # Reading the contents of the file
        with open("my_file.txt", 'r') as file:
            content = file.read()
        print("File contents:")
        print(content)
    except FileNotFoundError:
        print("File not found. Please ensure 'my_file.txt' exists.")
    except PermissionError:
        print("Permission denied. Unable to read the file.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    finally:
        print("File reading operation complete.")

def append_to_file():
    try:
        # Opening the file in append mode to add more lines
        with open("my_file.txt", 'a') as file:
            file.write("Appending a fourth line.\n")
            file.write("Adding another line with a number: 456.\n")
            file.write("Final line appended!\n")
        print("Text appended to file successfully.")
    except Exception as e:
        print(f"An error occurred during file append operation: {e}")
    finally:
        print("File append operation complete.")

# Running the functions in sequence
if __name__ == "__main__":
    create_file()
    read_file()
    append_to_file()
    read_file()  # Read again to see the appended content
