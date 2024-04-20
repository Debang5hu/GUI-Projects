#!/usr/bin/python3

# _*_ coding:utf-8 _*_


# NOTE: 
# clipboard  integration [done]
# user should be able to customize the password  [done]


# easily 60 character passwd can be seen on the screen according to the screen resolution


import tkinter
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
import string
#from itertools import permutations,combinations  # would crash for large value
from random import choice


# <--- global val --->
COLOR = '#c493ff'
file_path = ''
passwd = ''



# copy

def copyfunc():
    try:
        text = result.get("1.0", "end-1c")  # to get the text of the result entry
        screen.clipboard_clear()
        screen.clipboard_append(text)
    except tkinter.TclError:
        messagebox.showerror("Error", "No text selected")


# saving the password in a file
def save():
    if platform.get() != '':
        if file_path=='':
            files=[('Text Files', '*.txt')]
            file_name=asksaveasfilename(defaultextension = files)
            return 
        else:
            file_name=file_path

        if file_name is not None:
            if platform.get() != '':
                data = f'{platform.get()}:{passwd}'
            
                with open(file_name, 'a+') as fh:
                    fh.write(data)
    else:
        messagebox.showinfo('Not Saved','Enter Platform')


# clears the length field
def clear():
	plength.delete(0,tkinter.END);platform.delete(0,tkinter.END);result.delete('1.0',tkinter.END);passrule.delete(0,tkinter.END)



def charset():
    #charset
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation


    if str(passrule.get()) == '':
        return list(lower_case + upper_case + digits + punctuation)
    
    elif (str(passrule.get())).lower() == 'upper' or (str(passrule.get())).lower() == 'u':
        return list(lower_case + digits + punctuation)
    
    elif (str(passrule.get())).lower() == 'lower' or (str(passrule.get())).lower() == 'l':
        return list(upper_case + digits + punctuation)
    
    elif (str(passrule.get())).lower() == 'digit' or (str(passrule.get())).lower() == 'd':
        return list(lower_case + upper_case + punctuation)
    
    elif (str(passrule.get())).lower() == 'punctuation' or (str(passrule.get())).lower() == 'p':
        return list(lower_case + upper_case + digits)
    

############################################

def generate():  
    
    global passwd  
    
    try:
        if int(plength.get()) < 12:
            messagebox.showinfo(' ','For Security Reason The length of the password should be greater than equal to 12 ')
        elif int(plength.get()) > 60:
              messagebox.showinfo(' ','Oops! It exceed the screen resolution')
        else:
            wordlist = charset()  # getting the wordlist accordingly
            
            passwd = ''.join(choice(wordlist) for _ in range(int(plength.get())))
            #result.insert(text=f'{passwd}')
            result.delete('1.0', tkinter.END)
            result.insert(tkinter.END, passwd)

    except ValueError:
        messagebox.showinfo('Error','Enter Integer Only!')
		
#############################################    

if __name__ == '__main__':
    
    #screen
    screen = tkinter.Tk()
    screen.title("Password Generator")
    screen.geometry("750x300")
    screen.resizable(0,0)  # can't resize
    screen.configure(background=COLOR)


    # <--- widgets --->

    # label
    tkinter.Label(screen,text='Generator a Secure Password 🥷',background=COLOR,font=('monospace', 12)).place(x=50,y=40)

    tkinter.Label(screen,text='Enter the Length: ',background=COLOR,font=('monospace', 12)).place(x=50,y=80)
    plength = tkinter.Entry(screen)
    plength.place(x=250,y=80)


    tkinter.Label(screen,text='Platform: ',background=COLOR,font=('monospace', 12)).place(x=50,y=110)
    platform = tkinter.Entry(screen)
    platform.place(x=250,y=110)

    tkinter.Label(screen,text='Characters to exclude: ',background=COLOR,font=('monospace', 12)).place(x=50,y=140)
    passrule = tkinter.Entry(screen)
    passrule.place(x=250,y=140)
	
    # menubar
    menubar = tkinter.Menu(screen,background='#28282B',foreground='white')

	# save
    savemenu = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='Black')  # save the record in a txt file
    menubar.add_command(label='Save',command=save)


    screen.config(menu=menubar)

    # output area
    tkinter.Label(screen,text='Password: ',background=COLOR,font=('monospace', 12)).place(x=50,y=200)
    result = tkinter.Text(screen,height=1, width=61,bg=COLOR,font=('monospace', 12),highlightbackground='red')
    result.place(x=250,y=200)

    # password generate button
    generatebutton = tkinter.Button(screen,text='Generate',activeforeground='red',activebackground='black',bd=3,font='monospace',command=generate).place(x=250,y=250)
	
    clearbutton = tkinter.Button(screen,text='Clear',activeforeground='red',activebackground='black',bd=3,font='monospace',command=clear).place(x=100,y=250) # clear

    copybutton = tkinter.Button(screen,text='Copy',activeforeground='red',activebackground='black',bd=3,font='monospace',command=copyfunc).place(x=400,y=250)

    # to keep on runnig the screen
    screen.mainloop()