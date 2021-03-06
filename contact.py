import pyperclip
class Contact:
    """ 
    class that generates new instances of contacts 
    """
    contact_list = [] #empty contact list

    def save_contact(self):
        Contact.contact_list.append(self)

    # create new instances of a class
    def __init__(self,first_name,last_name,phone_number,email):
        
        self.first_name=first_name
        self.last_name=last_name
        self.phone_number=phone_number
        self.email=email 
    
    @classmethod
    def find_by_phone_number(cls,phone_number):

       for contact in cls.contact_list:
           if contact.phone_number==phone_number:
               return contact

    @classmethod
    def contact_exist(cls,phone_number):
        
        for contact in cls.contact_list:
            if contact.phone_number==phone_number:
                return True

        return False
    

    @classmethod
    def display_contacts(cls):
        return cls.contact_list

    @classmethod
    def copy_email(cls,phone_number):
        contact_found = Contact.find_by_phone_number(phone_number)
        pyperclip.copy(contact_found.email)
