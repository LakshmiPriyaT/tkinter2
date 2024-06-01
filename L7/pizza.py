from tkinter import *
#combobox is defined inside ttk
from tkinter.ttk import *
  
# Creating tkinter window 
window = Tk() 
window.title('Pizza App')
  
# label text for title 
title=Label(window, text = "Welcome to Pizza Hut")
# label 
caption=Label(window, text = "Select your Fav Pizza")
caption2=Label(window, text = "Select the qty of Pizza")
#place labels
title.grid(row = 0, column = 0,columnspan = 3, pady=25)
caption.grid(column = 0,row = 1,padx=10)
caption2.grid(column = 0,row = 2,padx=10)
# Combobox creation 
theNum = "Chicago Style"
numbers=Combobox(window,textvariable = theNum,width=10)   
# Adding combobox drop down list 
numbers['values'] = ("Chicago Style","Brick Oven Pizza","Italian Pizza","Neapolitan Pizza","California Pizza","New York Style Pizza","Sicilian Pizza","Greek Pizza")

theNum2 = IntVar()
numbers2=Combobox(window,textvariable = theNum2,width=10)   
# Adding combobox drop down list 
numbers2['values'] =tuple(range(10))

#radio buttons
endVal = "S"
r10=Radiobutton(window,text="S",variable=endVal,value="S")
r20=Radiobutton(window,text="M",variable=endVal,value="M")
r30=Radiobutton(window,text="L",variable=endVal,value="L")
#set the default value



#place radiobuttons and combobox
numbers.grid(column = 1, row = 1)
r10.grid(column = 2, row = 1)
r20.grid(column = 2, row = 2,padx=30)
r30.grid(column = 2, row = 3,padx=30)
numbers2.grid(column = 1, row = 2)

def generateMulTable():
    
    tables="You Ordered "+str(theNum2.get())+" "+str(endVal)+ " "+str(theNum) +" pizzas"
    table.configure(text=tables)

#create button and result table
generateButton=Button(window,text="Order",command=generateMulTable)
table=Label(window,anchor="center")

#place button and result table
generateButton.grid(row=4,column=1)
table.grid(row=5,column=1, pady = 25)


window.mainloop() 