#------------- @author: Srinath Sankragallu S-------------#
#-- A simple GUI to check reggular exppression in python--#
#-------contact: srinath.sankragallu@gmail.com------------#



import tkinter as tk 
from tkinter import ttk 
from tkinter import scrolledtext
import re
win = tk.Tk() 
win.title("ScrolledText Widget")

ttk.Label(win,  
          text = "Python Reggular Expression", 
          font = ("Times New Roman",15,'bold'),
          foreground = "black").grid(column = 0, 
                                     row = 0 , columnspan = 2) 
ttk.Label(win,  
          text = "Enter the regex:", 
          font = ("Times New Roman", 10),
          foreground = "black").grid(column = 0, 
                                     row = 1) 
e1 = tk.Entry(win)
e1.grid(column = 1 , row = 1)

ttk.Label(win,  
          text = "Enter the string:", 
          font = ("Times New Roman", 10),
          foreground = "black").grid(column = 0, 
                                     row = 2) 
e2 = tk.Entry(win)
e2.grid(column = 1 , row = 2)


text_area = scrolledtext.ScrolledText(win,  
                                      wrap = tk.WORD,  
                                      width = 40,  
                                      height = 10,  
                                      font = ("Times New Roman", 
                                              15)) 
  
text_area.grid(column = 0,row = 4 , columnspan=2 ,pady = 10, padx = 10)
text_area.tag_config('war' , foreground = 'red')
text_area.tag_config('result' , foreground = 'green')


def addtext(*st):
    text_area.insert(tk.INSERT,*st)
    
def do_stuff():
    reg = str(e1.get())
    st1 = e2.get()
    addtext(f'regex = {reg}\n')
    addtext(f'string = {st1}\n')
    try:
        res = str(re.findall(reg,st1))
        addtext(f'Result = {res}' ,'result' )
    except Exception as msg:
        addtext(msg , 'war')
    addtext('\n====================================\n')
    
b1 = tk.Button( win , text = 'Check' ,
               bg= 'green' , fg='white', 
               font = ("Times New Roman",12,'bold'),command = do_stuff )
b1.grid(row = 3 , column = 1)

win.mainloop() 
