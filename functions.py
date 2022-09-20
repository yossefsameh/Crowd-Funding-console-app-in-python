# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:09:26 2022

@author: Youssef
"""
from operations import askforstr,askfornum,askfordate,add_to_file,generate_new_id,readfile,overwrite_file


def createpro(usremail):
    title=askforstr('Please enter project name: ')
    desc=input('provide some details about this project: ')
    while True:
        if not desc:
            desc=input('provide some details about this project: ')
        else:
            break
    target=askfornum('please enter total target: ')
    start_date=askfordate('Please enter start date of this project: ')
    end_date=askfordate('Please enter end date of this project: ')
    owneremail=usremail
        
    details=[title,desc,str(target),str(start_date),str(end_date),owneremail]
    id = generate_new_id() #### prepare the data
    details.insert(0, str(id)) ### merge the book details into one line
    "join ---> join the list elements into one string using seperator "
    user_details = ":".join(details)
    ## save it in the file
    added=add_to_file(user_details,'projects.txt')
    if added:
        print("----project is created successfully ")
    else:
        print("---- error happened , try again now ")
        return createpro()
    
def listpro():
    allpro =readfile('projects.txt')
    if allpro==False:
        print('-----------no available projects ------ ')
    else:
        #for pro in allpro:
            #currpro = pro.strip("\n")
            #print(currpro)
        print(allpro)

def deletepro(usremail):
    allpro=readfile('projects.txt')
    print(allpro)
    pro_id = askfornum("please choose id of the project you want to delete: ")
    for pro in allpro:
        mypro = pro.strip("\n")
        mypro = mypro.split(":")
        if mypro[0]==str(pro_id) and mypro[6]==usremail:
            pro_index = allpro.index(pro)
            del allpro[pro_index]
            deleted=overwrite_file(allpro,'projects.txt')
            if deleted:
                print("---- project deleted successfully ---- ")
                return True
    print("project not found ")
    return False
    

def editpro(usremail):
    allpro=readfile('projects.txt')
    print(allpro)
    pro_id = askfornum("please choose id of the project you want to edit: ")
    for pro in allpro:
        mypro = pro.strip("\n")
        mypro = mypro.split(":")
        if mypro[0]==str(pro_id) and mypro[6]==usremail:
            pro_index = allpro.index(pro)
            del allpro[pro_index]
            deleted=overwrite_file(allpro,'projects.txt')
            title=askforstr('Please enter project name: ')
            desc=input('provide some details about this project: ')
            while True:
                if not desc:
                    desc=input('provide some details about this project: ')
                else:
                    break
            target=askfornum('please enter total target: ')
            start_date=askfordate('Please enter start date of this project: ')
            end_date=askfordate('Please enter end date of this project: ')
            owneremail=usremail
                
            details=[title,desc,str(target),str(start_date),str(end_date),owneremail]
            details.insert(0, str(pro_id)) ### merge the book details into one line
            "join ---> join the list elements into one string using seperator "
            user_details = ":".join(details)
            ## save it in the file
            added=add_to_file(user_details,'projects.txt')
            if added:
                print("----project is edited successfully ")
                return True
            else:
                print("---- error happened , try again now ")
                return editpro(usremail)
    print("project not found ")
    return False

def searchbydate():
    choice= input("1-search by start date, \n2-list end date \n") 
    if choice =="1":
        indate=askfordate('Please enter start date you want to search by: ')
    elif choice =="2":
        indate=askfordate('Please enter end date you want to search by: ')
    else:
        print('wrong input')
        return False    
    allpro=readfile('projects.txt')
    for pro in allpro:
        mypro = pro.strip("\n")
        mypro = mypro.split(":")
        if choice== "1":
            if mypro[4]==str(indate):
                print(mypro,'\n')
        elif choice=="2":
            if mypro[5]==str(indate):
                print(mypro,'\n')
        
        
        
        
        
        
        
        
        
        
        
        
        
        

