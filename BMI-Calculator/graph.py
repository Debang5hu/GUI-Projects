#!/usr/bin/python3

# _*_ coding:utf-8 _*_

# provide the file name

import matplotlib.pyplot as plt   #visualization
from sys import argv
from tkinter import messagebox


# global val
newdata = []

def draw():

    try:
        with open('graph.txt') as fh:
            data = fh.read().split('\n')
    except:
        messagebox.showinfo("ERROR", "File Not Found!")

    for x in data:
        separatedata = x.split(',')
        if len(separatedata) > 1:
            newdata.append(separatedata)
        else:
            pass
    
    # typecasting to int and float respectively and storing them to two array
    age = [int(x[0]) for x in newdata]
    bmi = [float(x[1]) for x in newdata]


    # beautifying the graph
    plt.plot(age, bmi, marker='o', linestyle='-', color='r')  #plotting

    plt.xlabel('Age')
    plt.ylabel('BMI')
    plt.title('BMI vs. Age')

    plt.grid(True)
    
    plt.show() #display
