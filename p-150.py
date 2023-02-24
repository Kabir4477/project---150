# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 15:23:13 2023

@author: drsau
"""

from tkinter import *
import random

root=Tk()
root.title("Luck friend Wheel")
root.geometry("500x500")

enter_country_name = Entry(root)
enter_country_name.place(relx=0.5,rely=0.2,anchor = CENTER)

enter_city_name = Entry(root)
enter_city_name.place(relx=0.5,rely=0.3,anchor = CENTER)


country_list = Label(root)
city_list = Label(root)
country_random = Label(root)
city_random = Label(root)

country_list = []
city_list = []

def addcountry():
    country_name = enter_country_name.get()
    country_list.append(country_name)
    country_list["text"] = " Country list : " + str(country_list)
def addcity():    
    city_name = enter_city_name.get()
    city_list.append(city_name)
    city_list["text"] = " City list : " + str(city_list)
    

    
def random_number():
    length = len(country_list)
    random_no = random.randint(0, length-1)
    index = country_list[random_no]
    country_random["text"] = "Random Country : " + str(index)
        
    length = len(city_list)
    random_no = random.randint(0, length-1)
    index1 = city_list[random_no]
    city_random["text"] = "Random City  : " + str(index1)
    
btn = Button(root, text = "Display Country And City" , command = random_number)
btn.place(relx=0.5,rely=0.4,anchor = CENTER)



btn1 = Button(root, text=" Display Random Country And City " , command = random_number)
btn1.place(relx=0.5,rely=0.6, anchor = CENTER)
country_random.place(relx=0.5,rely=0.7, anchor = CENTER)
city_random.place(relx=0.5,rely=0.8, anchor = CENTER)

root.mainloop()

