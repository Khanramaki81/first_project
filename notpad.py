#import library and classes
import tkinter
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
from tkinter.messagebox import *
from tkinter.filedialog import  *


# (1) creat a window and add a tltle to it with className
root = Tk(className="not_pad")

# (2) creat textbox and scrollbox in window form
text_scroll = scrolledtext.ScrolledText(root)
#determin the position of the text_scroll relative to window
text_scroll.pack()

# (4) creat menu in window form
menu_bar =Menu(root)

# (5) paste menu_bar to window
root.config(menu=menu_bar)
# (6) crat submenu in menu_bar form
submenu_1 = Menu(menu_bar)
submenu_2 =Menu(menu_bar)
submenu_3 =Menu(menu_bar)
submenu_4 =Menu(menu_bar)
submenu_5 =Menu(menu_bar)

# (7) add label and submenu to menu bar
menu_bar.add_cascade(label="File"  ,menu=submenu_1)
menu_bar.add_cascade(label="Edit"  ,menu=submenu_2)
menu_bar.add_cascade(label="Format",menu=submenu_3)
menu_bar.add_cascade(label="view"  ,menu=submenu_4)
menu_bar.add_cascade(label="Help"  ,menu=submenu_5)

# (9) add property opening  file select window
#rb . read line to line
def property_selectfile() :
    creatWindowSelectFile = tkinter.filedialog.askopenfile(parent=root,mode='rb',title='open  file')
    #if file selected .read and insert to text scroll then close the file
    if creatWindowSelectFile!=None :
        read_selectedFile=creatWindowSelectFile.read()
        text_scroll.insert("1.0",read_selectedFile)
        creatWindowSelectFile.close()

# (10) add property saveing  text
# mode write =w
def saveText():
    save_window= tkinter.filedialog.asksaveasfile(mode='w')
    #if user wants to saved file
    if save_window!=None:
        #get text of textbox and save_window read it
        textGeted=text_scroll.get('1.0',END+'-1c')
        save_window.write(textGeted)
        save_window.close()

# (11) add exit mode
def exit():
    if messagebox.askokcancel(title="Quit", message="do you want to exit  program ?"):
        root.destroy()

# (8) add label and identity to submenu label=File
submenu_1.add_command(label="open",command=property_selectfile)
submenu_1.add_command(label="save",command=saveText)
submenu_1.add_command(label="quit",command=exit)


root.mainloop()



