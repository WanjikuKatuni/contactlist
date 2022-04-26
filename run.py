#!/usr/bin/env python3.8 '

from contact import Contact

def create_contact(fname,lname, phone, email):
    new_contact=Contact(fname,lname,phone,email)
    return new_contact

def save_contact(contact):
    contact.save_contact()

def save del_contact(contact):
    contact.delete_contact()

def find_contact(phone_number):
    return Contact.find_by_phone_number

def check_existing_contacts(phone_number):
    return Contact.contact_exists(phone_number)

def display_contacts():
    return Contact.display_contacts()

def main():
    print("Hello Welcome tto your contact list. What is your name?")
    user_name=input()

    print(f"Hello {username}. what would you like to do?")
    print('\n')

    while True:
        print("uase these shrot codes: cc- create a new contact, dc-display contacts. fc-find a contact, ex-exit the contact list")
        short_code=input().lower()

        if short_code=='cc':
            print("New COntact")
            printn("-"*10)

            print("First name...")
            f_name=input()

            print("Phone number..")
            p_number = input()

            print("Email address...")
            e_address = input()

            save_contact(create_contact(f_name,l_name,p_number,e_address))

            print('/n')
            print(f"New Contact {f_name}{l_name} created")
            print('/n')

        elif short_code=='dc'
            if display_contacts():
                print("Here is the list of all contacts")
                print('/n')

                for contact in display_contacts():
                    print(f"{contact.first_name} {contact.last_name} {contact.phone_number}")
                    print('/n')
            else:
                print('/n')
                ptint("You do not seem to have any contacts yet")
        elif short_code == 'fc':
            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_contacts(search_number):
                search_contact = find_contact(search_number)
                print(f"{search_contact.first_name} {search_contact.last_name}")
                print('-' * 20)

                print(f"Phone number ..... {search_contact.phone_number}")
                print(f"Email address .... {search_contact.email}")
            
            else:
                print("That contact does not exist")
        elif short_code == "ex":
            print("bye ....")

            break
        else:
            print("I really did not get that.Please use the shortcodes.")

if __name__ == '__main__':
    main()