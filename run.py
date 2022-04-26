#!/usr/bin/env python3.8 '

from contact import Contact

def create_contact(fname,lname, phone, email):
    new_contact=Contact(fname,lname,phone,email)
    return new_contact