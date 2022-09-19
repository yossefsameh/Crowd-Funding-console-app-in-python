# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 18:25:04 2022

@author: Youssef
"""
import re
import datetime
import  time


def askforstr(message):
    mystr = input(message)
    if mystr.isspace() or not mystr or  not mystr.isalpha():
        print("---- please provide suitable string ")
        return askforstr(message)
    return mystr
def askfornum(message):
    mynum = input(message)
    try:
        mynum = int(mynum)
    except:
        print("---- please provide number not a string ---- ")
        return askfornum(message)
    else:
        return mynum

def askforemail_pk(message):
    email = input(message)
    regex= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.fullmatch(regex,email):
        allusers=readfile('users.txt')
        for user in allusers:
            curruser = user.strip("\n")
            curruser = curruser.split(":")
            if curruser[2]==email:
                print('Repeated email')
                return askforemail_pk(message)
        return email
    else:
        print("---- please enter a valid email")
        return askforemail_pk(message)
    
def askforemail(message):
    email = input(message)
    regex= re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    if re.fullmatch(regex,email):
        return email
    else:
        print("---- please enter a valid email")
        return askforemail(message)
    
def askfordate(message):
    mydate = input(message)
    regex= re.compile(r"^[0-3][0-9]/[0-3][0-9]/(?:[0-9][0-9])?[0-9][0-9]$")
    if re.fullmatch(regex,mydate):
        return mydate
    else:
        print("---- please enter a valid date dd/mm/yyyy")
        return askfordate(message)

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
        print("----- issue ")
        return False
    else:
        fileobj.write(f"{details}\n")
        return True
def overwrite_file(details,filepath):
    try:
     fileobj = open(filepath, "w")
    except:
        print('issue')
        return False
    else:
        fileobj.writelines(details)
        fileobj.close()
        return True
    
def readfile(filepath):
    try:
        fileobj = open(filepath)
    except Exception:
        print("---- error happened while openeing the file .. try again ")
        return False
    else:
        allfile = fileobj.readlines()
        fileobj.close()
        return allfile
def generate_new_id():
    id = round(time.time())
    return id

#def delete_pro_from_file(book_id):
    #pass
    
    
    
    
    
    
    
    
    
    
    
    
