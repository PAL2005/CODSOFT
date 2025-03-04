contacts = []  # Correcting variable name

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    
    contacts.append({
        'name': name,
        'phone': phone,
        'email': email,  # Fixing incorrect field assignment
        'address': address
    })
    
    print(f"Contact {name} added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("Contact List:")
        for contact in contacts:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}")
        print("")  # Removed incorrect indentation

def search_contact():
    query = input("Enter name or phone number to search: ")
    results = [c for c in contacts if query.lower() in c['name'].lower() or query in c['phone']]
    
    if results:
        for contact in results:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")
    else:
        print("No matching contacts found.\n")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = input("Enter new phone number: ")
            contact['email'] = input("Enter new email: ")
            contact['address'] = input("Enter new address: ")
            print(f"Contact {name} updated successfully!\n")
            return

    print("Contact not found.\n")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    global contacts
    contacts = [c for c in contacts if c['name'].lower() != name.lower()]
    print(f"Contact {name} deleted successfully!\n")

def main():
    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
