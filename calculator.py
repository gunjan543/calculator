from tkinter import *
root=Tk()
root.title("Calculator")
e=Entry(root,width=40,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button_add(number):
	current = e.get()
	e.delete(0,END)
	e.insert(0,str(current)+str(number))

def button_clear():
	e.delete(0,END)

def button_addition():
	first_number=e.get()
	global f_num
	f_num=int(first_number)
	global math
	math="addition"
	e.delete(0,END)

def button_equal():
	second_number=e.get()
	e.delete(0,END)

	if math=="addition":
		e.insert(0,f_num+int(second_number))
	if math=="subtraction":	
		e.insert(0,f_num-int(second_number))
	if math=="multiplication":	
		e.insert(0,f_num*int(second_number))
	if math=="division":	
		e.insert(0,f_num/int(second_number))

def button_sub():
	first_number=e.get()
	global f_num
	f_num=int(first_number)
	global math
	math="subtraction"
	e.delete(0,END)

def button_mul():
	first_number=e.get()
	global f_num
	f_num=int(first_number)
	global math
	math="multiplication"
	e.delete(0,END)

def button_div():
	first_number=e.get()
	global f_num
	f_num=int(first_number)
	global math
	math="division"
	e.delete(0,END)		


#defining buttons
button_1=Button(root,text='1',padx=40,pady=20,command=lambda:button_add(1))
button_2=Button(root,text='2',padx=40,pady=20,command=lambda:button_add(2))
button_3=Button(root,text='3',padx=40,pady=20,command=lambda:button_add(3))
button_4=Button(root,text='4',padx=40,pady=20,command=lambda:button_add(4))
button_5=Button(root,text='5',padx=40,pady=20,command=lambda:button_add(5))
button_6=Button(root,text='6',padx=40,pady=20,command=lambda:button_add(6))
button_7=Button(root,text='7',padx=40,pady=20,command=lambda:button_add(7))
button_8=Button(root,text='8',padx=40,pady=20,command=lambda:button_add(8))
button_9=Button(root,text='9',padx=40,pady=20,command=lambda:button_add(9))
button_0=Button(root,text='0',padx=40,pady=20,command=lambda:button_add(0))
button_sum=Button(root,text='+',padx=40,pady=52,command=button_addition)
button_subtract=Button(root,text='-',padx=40,pady=20,command=button_sub)
button_multiply=Button(root,text='*',padx=40,pady=20,command=button_mul)
button_divide=Button(root,text='/',padx=40,pady=20,command=button_div)
button_equal=Button(root,text='=',padx=87,pady=20,command=button_equal)
button_clear=Button(root,text='Clear',padx=30,pady=20,command=button_clear)

#put the buttons on screen
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)

button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)

button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_0.grid(row=4,column=0)
button_sum.grid(row=4,column=2,rowspan=2)
button_equal.grid(row=6,column=0,columnspan=2)
button_clear.grid(row=4,column=1)

button_subtract.grid(row=5,column=0)
button_multiply.grid(row=5,column=1)
button_divide.grid(row=6,column=2)

root.mainloop()