#!/usr/bin/python3

# _*_ coding:utf-8 _*_ 

# it will calculate Body Mass Index(BMI) using kg and m  [GUI]
# formula weight / height * height


import tkinter
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox   # popup
from graph import draw  # custom module for plotting the graph
from webbrowser import open_new_tab  # for reading about the project



# <--- global value --->
COLOR = '#444c69'   #hex
file_path = ''  # path for saving the file
BMI = 0

def aboutus():
	open_new_tab('https://github.com/Debang5hu/OIBSIP/blob/main/BMI-Calculator/README.md')


# graph representation
def data_visualisation():
	draw()


# to save the file record
def save():
	if file_path=='':
		files=[('Text Files', '*.txt')]
		file_name=asksaveasfilename(defaultextension = files)
	else:
		file_name=file_path

	if file_name is not None:
		data = f'\n{agefield.get()},{BMI}\n'    # way of storing data 18,24.24 [age,bmi]
		
		with open(file_name, 'a+') as fh:
			fh.write(data)



# clears the age,height and weight field
def clear():
	agefield.delete(0,tkinter.END)
	heightfield.delete(0,tkinter.END)   
	weightfield.delete(0,tkinter.END)

	# note: starts deleting from 0 index for (tkinter.Entry())  0.1 for tkinter.Text()

# it calculates the bmi
def calculate() -> float:
	global BMI
	try:
		height = float(heightfield.get())
		weight = float(weightfield.get())

		if height == 0:
			messagebox.showinfo("ERROR", "ERROR! Division by 0")
			result.config(text='ERROR! Division by 0')
			return

		BMI = round((weight / (height ** 2)),2)  # formula  [rounding up to 2 digits]

		# BMI conditions
		if BMI <= 18.5:
			result.config(text=f'{BMI} - Under Weight')
		elif BMI >= 18.5 and BMI <= 24.9:
			result.config(text=f'{BMI} - Healthy Weight') 
		elif BMI >= 25.0 and BMI <= 29.9:
			result.config(text=f'{BMI} - Over Weight') 
		elif BMI >= 30.0:
			result.config(text=f'{BMI} - Obesity ') 
		else:
			result.config(text='Check the value correctly')

	except ValueError:
		messagebox.showinfo("ERROR", "Enter Correct Value!")
		result.config(text='Enter Correct Value!')

# main
if __name__ == '__main__':

	#screen configurations
	screen = tkinter.Tk()
	screen.title("BMI Calculator")
	screen.geometry("550x400")
	screen.resizable(0,0)  # can't resize
	screen.configure(background=COLOR)


	# <--- widgets --->

	# age input
	tkinter.Label(screen,text='Age: ',background=COLOR,font=('monospace', 15)).place(x=50,y=50)
	agefield = tkinter.Entry(screen)
	agefield.place(x=200,y=50)

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
	savemenu = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white')  # save the record in a txt file
	menubar.add_command(label='Save',command=save)

	# graph
	graph = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white')  # exit 
	menubar.add_command(label='Graph',command=data_visualisation)

	# about
	about = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white')
	menubar.add_command(label='About',command=aboutus)

	# exit
	exit = tkinter.Menu(menubar, tearoff=False,background='#28282B',fg='white')  # exit 
	menubar.add_command(label='Exit',command=screen.destroy)

	screen.config(menu=menubar)
	#####################################################################################################################


	# to keep on runnig the screen
	screen.mainloop()
