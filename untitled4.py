# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 23:51:20 2022

@author: Youssef
"""

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
print(readfile('users.txt'))