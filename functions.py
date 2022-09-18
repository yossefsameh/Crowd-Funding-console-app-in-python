# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 20:09:26 2022

@author: Youssef
"""
from operations import askforstr,askfornum,askfordate,add_to_file,generate_new_id,readfile


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
        print(allpro)







