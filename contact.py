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
    
   