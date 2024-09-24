from tkinter import *
from customtkinter import *
import matplotlib.pyplot as plt
import torch
import math
import pywinstyles

def plot(x,y):
    plt.plot(x,y)
    plt.show()
x=torch.arange(0.,50.,0.1)


set_appearance_mode("light")
root=CTk()
root.geometry("500x500")

top_frame=CTkFrame(root,corner_radius=0,border_color="black")
top_frame.pack(padx=8,pady=8,fill="x")

def clear_callback():
    pass
clear_btn=CTkButton(top_frame,corner_radius=0,text="Clear",width=125,command=clear_callback)
clear_btn.grid(row=0,column=0)

entry=CTkEntry(top_frame,corner_radius=0,border_color="black",width=250)
entry.grid(row=0,column=1)

def plot_callback():
    pass
plot_btn=CTkButton(top_frame,corner_radius=0,text="Plot Function",width=125,command=plot_callback)
plot_btn.grid(row=0,column=2)
root.mainloop()




