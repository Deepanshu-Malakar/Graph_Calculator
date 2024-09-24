from tkinter import *
from customtkinter import *
import matplotlib.pyplot as plt
import torch
from math import *
import pywinstyles

def plot(x,y):
    plt.figure(figsize=(10,8))
    plt.plot(x,y)
    plt.show()
x=torch.arange(0.,50.,0.1)


set_appearance_mode("light")
root=CTk(fg_color="white")
root.title("Graph Calculator")
# root.geometry("516x500")
pywinstyles.apply_style(root,"acrylic")

class key:
    def __init__(self,master,text,color,row,column,text_color="black") -> None:
        self.button=CTkButton(master,text=text,fg_color=color,command=self.click,corner_radius=0,width=100,text_color=text_color,bg_color="transparent")
        # pywinstyles.set_opacity(self.button,0.8)
        self.text=text
        self.button.grid(row=row,column=column)
    def click(self):
        if(self.text=="clear"):
            entry.delete(0,END)
        elif(self.text=="log"):
            entry.insert(END,"torch.log10(")
        elif(self.text=="sin"):
            entry.insert(END,"torch.sin(")
        elif(self.text=="cos"):
            entry.insert(END,"torch.cos(")
        elif(self.text=="tan"):
            entry.insert(END,"torch.tan(")
        elif(self.text=="e"):
            entry.insert(END,"torch.exp(")
        else:
            entry.insert(END,self.text)



purple="#b283ff"
blue="#6ea4ea"

top_frame=CTkFrame(root,corner_radius=0,border_color="black",fg_color="transparent",bg_color="transparent")
top_frame.pack(padx=8,pady=8,fill="x")
pywinstyles.set_opacity(top_frame,0.8)

bottom_frame=CTkFrame(root,corner_radius=0,fg_color="transparent",bg_color="transparent")
bottom_frame.pack(fill="x",padx=8,pady=8)
pywinstyles.set_opacity(bottom_frame,0.8)


fx_btn=CTkButton(top_frame,corner_radius=0,text="F(x) =",width=100,text_color="black",fg_color=blue)
fx_btn.grid(row=0,column=0)

entry=CTkEntry(top_frame,corner_radius=0,border_color="black",width=300,border_width=1)
entry.grid(row=0,column=1)

def plot_callback():
    query=entry.get()
    y=eval(query)
    plot(x,y)

plot_btn=CTkButton(top_frame,corner_radius=0,text="Plot Function",width=100,command=plot_callback,text_color="black",fg_color=blue)
plot_btn.grid(row=0,column=2)

log_btn=key(bottom_frame,"log",purple,0,0)
e_btn=key(bottom_frame,"e",purple,1,0)
exp_btn=key(bottom_frame,"**",purple,2,0)
dot_btn=key(bottom_frame,".",purple,3,0)
sin_btn=key(bottom_frame,"sin",blue,4,0)
cos_btn=key(bottom_frame,"cos",blue,4,1)
tan_btn=key(bottom_frame,"tan",blue,4,2)
x_btn=key(bottom_frame,"x",blue,4,3)
clear_btn=key(bottom_frame,"clear",blue,4,4)

btn7=key(bottom_frame,"7","white",0,1)
btn8=key(bottom_frame,"8","white",0,2)
btn9=key(bottom_frame,"9","white",0,3)

btn4=key(bottom_frame,"4","white",1,1)
btn5=key(bottom_frame,"5","white",1,2)
btn6=key(bottom_frame,"6","white",1,3)

btn1=key(bottom_frame,"1","white",2,1)
btn2=key(bottom_frame,"2","white",2,2)
btn3=key(bottom_frame,"3","white",2,3)

bracket_btn_C=key(bottom_frame,"(","white",3,1)
bracket_btn_D=key(bottom_frame,")","white",3,3)
btn0=key(bottom_frame,"0","white",3,2)

plus_btn=key(bottom_frame,"+",purple,0,4)
minus_btn=key(bottom_frame,"-",purple,1,4)
into_btn=key(bottom_frame,"*",purple,2,4)
devide_btn=key(bottom_frame,"/",purple,3,4)


root.mainloop()




