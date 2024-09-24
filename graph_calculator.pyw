from tkinter import *
from customtkinter import *
import matplotlib.pyplot as plt
import torch
import math

x=torch.arange(0.,50.,0.1)
# print(x)
def plot(x,y):
    plt.figure(figsize=(10,2))
    plt.scatter(x,y,c="b",s=4)
    plt.show()
y=[math.sin(i) for i in x]
# y=x*x
# print(y)

plt.plot(x,y)
plt.show()