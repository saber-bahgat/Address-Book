# IMPORTING
import sqlite3

# Connecting with DB
conn = sqlite3.connect("address_book.db")
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        phone_number TEXT NOT NULL UNIQUE,
        mail TEXT NOT NULL UNIQUE,
        address TEXT NOT NULL
    )
""")
conn.commit()

# Functions

def add_contact(name, phone_number, mail, address):
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO contacts (name, phone_number, mail, address) VALUES (?, ?, ?, ?)", (name, phone_number, mail, address))
    conn.commit()
    conn.close()

def update_contact(new_name, new_phone_number, new_mail, new_address, name):
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()
    cur.execute("UPDATE contacts SET name = ?, phone_number = ?, mail = ?, address = ? WHERE name = ?", (new_name, new_phone_number, new_mail, new_address, name))
    conn.commit()
    conn.close()

def display_contacts():
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    data_contacts = cur.fetchall()
    conn.close()
    return data_contacts

def search_contact(search):
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts WHERE name LIKE ?", ('%' + search + '%',))
    search_contacts = cur.fetchall()
    conn.close()
    return search_contacts

def delete_contact(name):
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE name = ?", (name,))
    conn.commit()
    conn.close()

def contact_exists(name):
    conn = sqlite3.connect("address_book.db")
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM contacts WHERE name = ?", (name,))
    exists = cur.fetchone() is not None
    conn.close()
    return exists

def main():
    print("------------------------------ADDRESS BOOK------------------------------")
    while True:
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Display Contacts")
        print("4. Search Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            print("-" * 15)
            print("# Add Contact!")
            name = input("Enter the Name: ")
            phone_number = input("Enter the Phone Number: ")
            mail = input("Enter the Mail (None for skip): ")
            address = input("Enter the Address (None for skip): ")
            add_contact(name, phone_number, mail, address)
            print("Content Added Successfully!!")
            print("-" * 15)

        elif choice == '2':
            print("-" * 15)
            print("# Update Contact!")
            name = input("Enter the name of contact to update: ")
            if contact_exists(name):
                new_name = input("Enter the New Name: ")
                new_phone_number = input("Enter the New Phone Number: ")
                new_mail = input("Enter the New Mail (None for skip): ")
                new_address = input("Enter the New Address (None for skip): ")
                update_contact(new_name, new_phone_number, new_mail, new_address, name)
                print("Content Updated Successfully!!")
                print("-" * 15)
            else:
                print("Contact not found!")
        
        elif choice == '3':
            print("-" * 15)
            print("# Display Contacts!")
            contacts = display_contacts()
            for contact in contacts:
                print(f"[{contact[0]}] {contact[1]}  |  Phone Number: {contact[2]}")
                print(f"Mail: {contact[3]}  |  Address: {contact[4]}")
                print()   
            print("-" * 15)

        elif choice == '4':
            print("-" * 15)
            print("# Search Contact!")
            while True:
                search = input("Enter the name to search (ex for exit): ")
                if search == 'ex':
                    break
                results = search_contact(search)
                if results:
                    for contact in results:
                        print(f"[{contact[0]}] {contact[1]}  |  Phone Number: {contact[2]}")
                        print(f"Mail: {contact[3]}  |  Address: {contact[4]}")
                        print()
                    break
                else:
                    print("Contact not found!")
            print("-" * 15)

        elif choice == '5':
            print("-" * 15)
            print("# Delete Contact!")
            while True:
                name = input("Enter the name of contact to delete (ex for exit): ")
                if name == 'ex':
                    break
                if contact_exists(name):
                    delete_contact(name)
                    print("Contact Deleted Successfully!!")
                    print("-" * 15)
                    break
                else:
                    print("Contact not found!")

        elif choice == '6':
            print("Thanks for trying our app, Have a nice day!")
            break

        else:
            print("Invalid choice, please select a number between 1 and 6!")
# Runing code
if __name__ == '__main__':
    main()