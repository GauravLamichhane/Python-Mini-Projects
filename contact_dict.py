import json
import os

FILE = "contacts.json"

# Load existing contacts from file
def load_contacts():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=4)

# Create or update contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts[name] = {"phone": phone, "email": email}
    print(f"Contact {name} saved!")

# View contact
def view_contact(contacts):
    name = input("Enter name to view: ")
    if name in contacts:
        print(f"Name: {name}")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
    else:
        print("Contact not found!")

# View all contacts
def view_all_contacts(contacts):
    if not contacts:
        print("No contacts found!")
        return
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted!")
    else:
        print("Contact not found!")

# Main menu
def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Mini Contact Book ---")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. View All Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contact(contacts)
        elif choice == "3":
            view_all_contacts(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

#only run main() if this file is executed directly
#If the file is imported in anothery python script, main() wont run automatically
if __name__ == "__main__":
    main()
