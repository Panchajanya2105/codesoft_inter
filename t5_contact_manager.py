class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        new_contact = Contact(name, phone, email, address)
        self.contacts.append(new_contact)
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("\n Contact List:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact.name.lower() or search_term in contact.phone]
        if results:
            print("\nSearch Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}")
        else:
            print("No contacts found.")

    def update_contact(self, old_name, new_name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact.name.lower() == old_name.lower():
                contact.name = new_name
                contact.phone = new_phone
                contact.email = new_email
                contact.address = new_address
                print(f"Contact '{old_name}' updated successfully.")
                return
        print(f"Contact '{old_name}' not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                self.contacts.remove(contact)
                print(f"Contact '{name}' deleted successfully.")
                return
        print(f"Contact '{name}' not found.")

def main():
    manager = ContactManager()
    
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            manager.add_contact(name, phone, email, address)

        elif choice == '2':
            manager.view_contacts()

        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            manager.search_contact(search_term)

        elif choice == '4':
            old_name = input("Enter the name of the contact to update: ")
            new_name = input("Enter new name: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            manager.update_contact(old_name, new_name, new_phone, new_email, new_address)

        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '6':
            print("Exiting the Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
