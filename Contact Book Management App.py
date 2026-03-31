contacts = {}

while True:
    print("\nContact Book Management App")
    print("1. Add a new contact")
    print("2. View contact")
    print("3. Update a contact")
    print("4. Delete a contact")
    print("5. Search for a contact")
    print("6. Count total contacts")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        name = input("Enter contact name: ")
        if name in contacts:
            print(f"Contact {name} already exists.")
        else:
            age = input("Enter contact age: ")
            email = input("Enter contact email: ")
            mobile = input("Enter contact mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print("Contact added successfully.")
    elif choice == '2':
        name = input("Enter contact name to view: ")
        if name in contacts:
            contact = contacts[name]
            print(f'Name: {name}, Age: {age}, Email: {email}, Mobile: {mobile}')
        else:
            print("Contact not found.")
    elif choice == '3':
        name = input("Enter contact name to update: ")
        if name in contacts:
            age = input("Enter new contact age: ")
            email = input("Enter new contact email: ")
            mobile = input("Enter new contact mobile number: ")
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print("Contact updated successfully.")
        else:
            print("Contact not found.")
    elif choice == '4':
        name = input("Enter contact name to delete: ")
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print("Contact not found.")
    elif choice == '5':
        search_name = input("Enter contact name to search: ")
        found = False
        for name, contact in contacts.items():
            if search_name.lower() == name.lower():
                print(f'Name: {name}, Age: {age}, Email: {email}, Mobile: {mobile}')
                found = True
                break
        if not found:
            print("Contact not found.")
    elif choice == '6':
        print(f'Total contacts in your book: {len(contacts)}')
    elif choice == '7':
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")