# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:25:04 2022

@author: Youssef
"""
import re

def askforstr(message):
    mystr = input(message)
    if mystr.isspace() or not mystr or  not mystr.isalpha():
        print("---- please provide suitable string ")
        return askforstr(message)
    return mystr

def askforemail(message):
    email = input(message)
    regex= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.fullmatch(regex,email):
        return email
    else:
        print("---- please enter a valid email")
        return askforemail(message)

def askforpassword(message):
    password = input(message)
    if password.isspace() or not password or len(password)<8 or len(password)>20:
        print("password can not contain spaces\n password must be greater then 7 character and less than 21 characters ")
        return askforpassword(message)
    return password

def confirm_password(correct_password):
    confirmed_password = input("Please Confirm your Password: ")
    if confirmed_password == correct_password:
        return confirmed_password
    print('you entered wrong password')
    return confirm_password(correct_password)

def askforphone(message):
    phone = input(message)
    regex = re.compile(r"^[010,011,012]\d{10}")
    if re.fullmatch(regex,phone):
        return phone
    else:
        print("---- please enter a valid phone")
        return askforphone(message)
    
def add_to_file(details,filepath):
    try:
        fileobj=open(filepath, "a")
    except:
        print("----- issue while registration ")
        return False
    else:
        fileobj.write(f"{details}\n")
        return True

def readfile(filepath):
    try:
        fileobj = open(filepath)
    except Exception as e:
        print("---- error happened while openeing the file .. try again ")
        return False
    else:
        allfile = fileobj.readlines()
        fileobj.close()
        return allfile