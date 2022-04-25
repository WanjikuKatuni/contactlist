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

if __name__ == '__main__':
    unittest.main()