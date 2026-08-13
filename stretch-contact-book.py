"""
Stretch Exercise: Contact Book Menu
Student: Subhan Karki
Day: 2
"""

# Dictionary to store contacts (nested dictionary structure)
# Format: { "Name": {"phone": "...", "email": "..."}, ... }
contacts = {}

while True:
    print("\n--- Contact Book Menu ---")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. Display all contacts")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ").strip()
    
    if choice == "1":
        print("\n--- Add Contact ---")
        name = input("Enter name: ").strip().title()
        if not name:
            print("Name cannot be empty.")
            continue
            
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip().lower()
        
        # Store using nested dictionary
        contacts[name] = {
            "phone": phone,
            "email": email
        }
        print(f"Contact '{name}' added successfully!")
        
    elif choice == "2":
        print("\n--- Search Contact ---")
        name = input("Enter name to search: ").strip().title()
        
        # Safely search without crashing if the contact doesn't exist
        if name in contacts:
            print(f"Found Contact -> Name: {name}")
            print(f"  Phone: {contacts[name]['phone']}")
            print(f"  Email: {contacts[name]['email']}")
        else:
            print(f"Contact '{name}' not found in the contact book.")
            
    elif choice == "3":
        print("\n--- Delete Contact ---")
        name = input("Enter name to delete: ").strip().title()
        
        # Safely delete without crashing if the contact doesn't exist
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted successfully.")
        else:
            print(f"Contact '{name}' does not exist.")
            
    elif choice == "4":
        print("\n--- All Contacts ---")
        if not contacts:
            print("The contact book is currently empty.")
        else:
            for name, details in contacts.items():
                print(f"Name: {name}")
                print(f"  Phone: {details['phone']}")
                print(f"  Email: {details['email']}")
                print("-" * 20)
                
    elif choice == "5":
        print("Exiting Contact Book. Goodbye!")
        break
        
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")