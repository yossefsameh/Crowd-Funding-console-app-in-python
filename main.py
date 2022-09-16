# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:54:45 2022

@author: Youssef
"""
import user_login
def mainmenu():
    while True:
        choice= input("1-Login, 2-Registe, 3-exit \n")
        if choice =="1":
            user_login.login()
        elif choice =="2":
            user_login.register()
        elif choice=="3":
            break
        else:
            print("---- no correct choice ----")
            return mainmenu()

mainmenu()