import os
import json

FILENAME = "contacts.json"


def load_contacts():
  if os.path.exists(FILENAME):
    with open(FILENAME,"r") as f:
      return json.load(f)
  return {}

def add_contact(contacts):
  name = input("Enter the name: ")
  phone = input("Enter the phone: ")
  email = input("Enter the email: ")
  #in this phase the changes are only in RAM not saved to file yet
  contacts[name] = {"phone":phone,"email":email}
  print(f"Contact {name} saved!")

def view_contact(contacts):
  name = input("Enter the name to view:")
  if name in contacts:
    print(f"Name:{name}\n")
    print(f"Phone:{contacts[name]['phone']}\n")
    print(f"Email:{contacts[name]['email']}\n")
  else:
    print("Contact not found")

def view_all_contacts(contacts):
  if not contacts:
    print("No contacts found!")
    return
  #keys -> names ("Alice","Bob")
  #values -> another dict with phone and email
  #contact.items() retur all key value pairs of the dict as tuples
  #used when you want both key and value in a loop
  for name,info in contacts.items():
    print(f"Name:{name},Phone:{info['phone']},Email:{info['email']}")

def delete_contact(contacts):
  name = input("Enter the name to delete: ")
  if name in contacts:
    del contacts[name]
    print(f"Contact:{name} deleted..")
  else:
    print("contact not found ")

def save_contact(contacts):
  with open("contacts.json",'w') as f:#open file in write mode
    json.dump(contacts,f,indent=4)#convert dict to json


def main():
  contacts = load_contacts()
  while True:
    print("\n--- Mini Contact Book ---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. View All Contacts")
    print("4. Delete Contact")
    print("5. Exit")
    
    choice = input("Enter the choice: ")
    if choice == "1":
      add_contact(contacts)
    elif choice == "2":
      view_contact(contacts)
    elif choice == "3":
      view_all_contacts(contacts)
    elif choice == "4":
      delete_contact(contacts)
    elif choice == "5":
      save_contact(contacts)
      break
    else:
      print("Invalid choice try again!")

#it will get executed if the script is run directly will not run if the script is being imported as module
if __name__ == "__main__":
  main()
