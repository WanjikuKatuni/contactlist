import unittest #python test framework
from contact import Contact

class TestContact(unittest.TestCase): #subclass that inherits uniitest.testcase
    """
    Test class which defines test cases for the contact class

    Args: unittest.Testcase:TestCAse class that assists in creating test cases
    """

    def setUp(self):
        "setUp used to define methods that will be executed before the test method"

        self.new_contact = Contact("ann","wanjiku","254704216527","shiko@gmail.com") #setUp creates new instance of Contact

    def test_init(self): #test method defined
       
        #checks for an expected result
        
        self.assertEqual(self.new_contact.first_name,"ann")
        self.assertEqual(self.new_contact.last_name,"wanjiku")
        self.assertEqual(self.new_contact.phone_number,"254704216527")
        self.assertEqual(self.new_contact.email,"shiko@gmail.com")

    def test_save_contact(self):
        self.new_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),1)

    def tearDown(self):
        """ clears test cases """
        Contact.contact_list=[]


    def test_save_multiple_contact(self): #test case to test if we can asave multiple contacts
        self.new_contact.save_contact()
        test_contact=Contact("Test","user","2547000000","test@user.com") #test contact object created
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2) #checking

    def test_find_contact_by_phone_number(self):

        self.new_contact.save_contact()
        test_contact=Contact("Test","user","2547000000","test@user.com") #test contact object created
        test_contact.save_contact()

        found_contact = Contact.find_by_phone_number("2547000000")

        self.assertEqual(found_contact.email,test_contact.email)
    
    def test_contact_exists(self):

        self.new_contact.save_contact()
        test_contact=Contact("Test","user","2547000000","test@user.com") #test contact object created
        test_contact.save_contact()

        contact_exists = Contact.contact_exist("2547000000")

        self.assertTrue(contact_exists) #check if return value is true

    def test_display_all_contacts(self):
        self.assertEqual(Contact.display_contacts(), Contact.contact_list)

if __name__ == '__main__':
    unittest.main()