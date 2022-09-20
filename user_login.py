# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:17:51 2022

@author: Youssef
"""

from operations import askforstr,askforemail_pk,askforemail,askforpassword,confirm_password,askforphone,add_to_file,readfile
import functions
def register():
    firstname=askforstr('Please enter your First Name: ')
    lastname=askforstr('Please enter your Last Name: ')
    email=askforemail_pk('Please enter your email: ')
    password=askforpassword('Please enter a password: ')
    confirmed_password=confirm_password(password)
    phone=askforphone('Please enter your phone number: +2')
    
    details=[firstname,lastname,email,password,phone]
    #id = generate_new_id() #### prepare the data
    #details.insert(0, str(id)) ### merge the book details into one line
    "join ---> join the list elements into one string using seperator "
    user_details = ":".join(details)
    ## save it in the file
    added=add_to_file(user_details,'users.txt')
    if added:
        print("----registration is done successfully ")
    else:
        print("---- error happened , try again now ")
        return register()
    
def login():
    email=askforemail('Please enter your email: ')
    password=askforpassword('Please enter your password: ')
    allusers=readfile('users.txt')
    for user in allusers:
        curruser = user.strip("\n")
        curruser = curruser.split(":")
        if curruser[2]==email and curruser[3]==password:
            return menu(email)
    print("wrong email or password ")
    return False

def menu(usremail):    
    while True:
        choice= input("1-Creat new project, \n2-list projects,\n3-edit prohect, \n4-delete project, \n5-search by date \n6-back to main menu \n")
        if choice =="1":
            functions.createpro(usremail)
        elif choice =="2":
            functions.listpro()
        elif choice =="3":
            functions.editpro(usremail)
        elif choice =="4":
            functions.deletepro(usremail)
        elif choice =="5":
            functions.searchbydate()
        elif choice=="6":
            break
        else:
            print("---- no correct choice ----")
            return menu(usremail)
        
        
        
        
        
        