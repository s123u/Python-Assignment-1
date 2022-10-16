import tkinter as tk
from tkinter import *
root =Tk()
root.geometry("500x500")
def getCourseList():
    selectedCourses=[]
    curSelected=lb.curselection()
    for i in curSelected:
        c=lb.get(i)
        
