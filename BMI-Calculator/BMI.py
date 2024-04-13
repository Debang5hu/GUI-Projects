#!/usr/bin/python3

# _*_ coding:utf-8 _*_ 

# it will calculate Body Mass Index(BMI) using kg and m  [GUI]
# formula weight / height * height

import tkinter
from tkinter.filedialog import asksaveasfilename  

try:
	from ctypes import windll,byref,sizeof,c_int
except:
	pass



# <--- global value --->
COLOR = '#444c69'   #hex
file_path = ''  # path for saving the file
val = ''   # empty string


# border color of the screen
def bordercolor():
	try:
		HWND=windll.user32.GetParent(screen.winfo_id())
		title_color=0x00000000
		windll.dwmapi.DwmSetWindowAttribute(
			HWND,
			35,
			byref(c_int(title_color)),
			sizeof(c_int))
	except:
		pass


# have to fix this!
# to save the file record
def save():
	if file_path=='':
		files=[('Text Files', '*.txt')]
		file_name=asksaveasfilename(defaultextension = files)
	else:
		file_name=file_path

	if file_name is not None:
		data = f'Height = {heightfield.get()}\nWeight = {weightfield.get()}\nBMI = {val}'
		
		with open(file_name, 'w') as fh:
			fh.write(data)



# clears the height and weight field
def clear():
	heightfield.delete(0,tkinter.END)   
	weightfield.delete(0,tkinter.END)

	# note: starts deleting from 0 index for (tkinter.Entry())  0.1 for tkinter.Text()

# it calculates the bmi
def calculate() -> float:
	global val
	try:
		height = float(heightfield.get())
		weight = float(weightfield.get())

		BMI = weight / (height ** 2)

		if BMI <= 18.5:
			val = f'{round(BMI,2)} - Under Weight'  # to print upto 2 decimal point 
			result.config(text=val) 
		elif BMI >= 18.5 and BMI <= 24.9:
			val = f'{round(BMI,2)} - Healthy Weight'  # to print upto 2 decimal point 
			result.config(text=val) 
		elif BMI >= 25.0 and BMI <= 29.9:
			val = f'{round(BMI,2)} - Over Weight'  # to print upto 2 decimal point 
			result.config(text=val) 
		elif BMI >= 30.0:
			val = f'{round(BMI,2)} - Obesity' # to print upto 2 decimal point 
			result.config(text=f'{round(BMI,2)} - Obesity ') 
		else:
			val = 'Check the value correctly'
			result.config(text=val)

	except ValueError:
		result.config(text='Enter Correct Value!')

# main
if __name__ == '__main__':

	#screen configurations
	screen = tkinter.Tk()
	screen.title("BMI Calculator")
	bordercolor()  # change the default border color [only works in windows :( ]
	screen.geometry("550x400")
	screen.resizable(0,0)  # can't resize
	screen.configure(background=COLOR)


	# <--- widgets --->

	# height input
	tkinter.Label(screen,text='Height [m]: ',background=COLOR,font=('monospace', 15)).place(x=50,y=100)
	heightfield = tkinter.Entry(screen)
	heightfield.place(x=200,y=100)

	# weight input
	tkinter.Label(screen,text='Weight [kg]: ',background=COLOR,font=('monospace', 15)).place(x=50,y=150)
	weightfield = tkinter.Entry(screen)
	weightfield.place(x=200,y=150)

	# output display area
	tkinter.Label(screen,text='BMI: ',background=COLOR,font=('monospace', 15)).place(x=50,y=200)

	result = tkinter.Label(screen,text='0',background=COLOR,font=('monospace', 15))
	result.place(x=200,y=200)


	# buttons
	calculatebutton = tkinter.Button(screen,text='Calculate',activeforeground='red',activebackground='black',bd=3,font='monospace',command=calculate).place(x=200,y=250) # calculate

	clearbutton = tkinter.Button(screen,text='Clear',activeforeground='red',activebackground='black',bd=3,font='monospace',command=clear).place(x=100,y=250) # clear


	#####################################################################################################################
	# menubar
	menubar = tkinter.Menu(screen,background='#28282B',foreground='white')

	# save
	save = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white')  # save the record in a txt file
	menubar.add_command(label='Save',command=save)

	# exit
	exit = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white')  # exit 
	menubar.add_command(label='Exit',command=screen.destroy)

	screen.config(menu=menubar)
	#####################################################################################################################


	# to keep on runnig the screen
	screen.mainloop()
