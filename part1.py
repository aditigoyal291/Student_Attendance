from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Face_Recognition_System:
    def _init_(self,root):
        self.root=root
        self.root.geometry("1500x800")
        self.root.title("Student Attendance Management System")



if _name_=="_main_":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()