import os

def create_file(file_name):
    try:
        with open(file_name, 'x') as file:
            file.write('')
        print(f"File '{file_name}' created successfully.")
        
    except FileExistsError:
        print(f"File '{file_name}' already exists.")
        
    except Exception as E:
        print(f"Error creating file: {E}")
        
def view_all_files(file_name):
    files = os.listdir()
    if not files:
        print("No files found in the current directory.")
    else:
        print("Files in the current directory:")
        for file in files:
            print(file)
            
def delete_file(file_name):
    try:
        os.remove(file_name)
        print(f"File '{file_name}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as E:
        print(f"Error deleting file: {E}")
        
def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(f"Content of '{file_name}':\n{content}")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as E:
        print(f"Error reading file: {E}")
        
def edit_file(file_name):
    try:
        with open(file_name, 'a') as file:
            new_content = input("Enter the content to add to the file: ")
            file.write(new_content + '\n')
        print(f"Content added to '{file_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
    except Exception as E:
        print(f"Error editing file: {E}")
        
def main():
    while True:
        print("\nFile Management App")
        print("1. Create a new file")
        print("2. View all files")
        print("3. Delete a file")
        print("4. Read a file")
        print("5. Edit a file")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            file_name = input("Enter the name of the file to create: ")
            create_file(file_name)
        elif choice == '2':
            view_all_files('')
        elif choice == '3':
            file_name = input("Enter the name of the file to delete: ")
            delete_file(file_name)
        elif choice == '4':
            file_name = input("Enter the name of the file to read: ")
            read_file(file_name)
        elif choice == '5':
            file_name = input("Enter the name of the file to edit: ")
            edit_file(file_name)
        elif choice == '6':
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
            
if __name__ == "__main__":
    main()