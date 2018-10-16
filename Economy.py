from tkinter import *

def main():
    print("Application Running")

if __name__ == '__main__':
    main()

root = Tk()

ent = Entry(root)
interest_field = Entry(root)
years_field = Entry(root)
switch_variable1 = IntVar()
switch_variable2 = IntVar()
switch_variable1.set(0)
switch_variable2.set(0)
Choice1 = 0
choice2 = 0
answer = 0.0

root.title("Formula calculator")
root.geometry('500x450')
    
Label(root, 
    text="Formula Calculator",
	fg = "red", bg="White",
    font = "Helvetica 30 bold italic").pack()

Label(root,text = "Enter Interest").pack()
interest_field.pack()
Label(root,text = "Enter Number of years").pack()
years_field.pack()

def setValues():
    global Choice1,Choice2
    Choice1 = switch_variable1.get()
    Choice2 = switch_variable2.get()

def CalcPrincipal(x):
    interest = float(interest_field.get())
    years = int(years_field.get())
    interest = interest/100;
    temp1 = pow((1+interest),years)
    val = 0.0
    if x==2:
        val = temp1 - 1.0
        val = val/interest
        val = val/temp1
    else:
        val = 1.0
        val = val/temp1
    return val*float(ent.get())

def CalcAmount(x):
    interest = float(interest_field.get())
    years = int(years_field.get())
    
    interest = interest/100.0;
   
    temp1 = pow((1.0+interest),years)
    
    val = 0.0
    if x==1:
        val = (interest*temp1)/(temp1-1)
    if x==3:
        val = interest
        val = val/(temp1-1.0)
    if x==4:
        temp2 = temp1-1
        temp2 = years/(temp2)
        val = 1/interest
        val = val - temp2
    return val*float(ent.get())

def CalcFutureWorth(x):
    interest = float(interest_field.get())
    years = int(years_field.get())

    interest = interest/100;
    
    temp1 = pow((1.0+interest),years)
    val = 0.0
    if x==1:
        val = temp1
    else:
        val = temp1-1.0
        val = val/interest
    return val*float(ent.get())

def evaluate():
    global answer

    if Choice1 == 1:
        answer = CalcPrincipal(Choice2)
    if Choice1 == 2:
        answer = CalcAmount(Choice2)
    if Choice1 == 3:
        answer = CalcFutureWorth(Choice2)
    print("The answer is = ",answer)

Label(root, text="To Find",pady="10").pack()
switch_frame = Frame(root)
switch_frame.pack()

F_button = Radiobutton(switch_frame, text="Principle", variable=switch_variable1,
                            indicatoron=False, value=1, width=10,command=setValues)
P_button = Radiobutton(switch_frame, text="Amount", variable=switch_variable1,
                            indicatoron=False, value=2, width=10,command=setValues)
A_button = Radiobutton(switch_frame, text="Future Worth", variable=switch_variable1,
                            indicatoron=False, value=3, width=10,command=setValues)
F_button.pack(side="left")
P_button.pack(side="left")
A_button.pack(side="left")
    

Label(root, text="Given",pady="10").pack()
switch_frame = Frame(root)
switch_frame.pack()
    
F_button = Radiobutton(switch_frame, text="Principle", variable=switch_variable2,
                            indicatoron=False, value=1, width=10,command=setValues)
P_button = Radiobutton(switch_frame, text="Amount", variable=switch_variable2,
                            indicatoron=False, value=2, width=10,command=setValues)
A_button = Radiobutton(switch_frame, text="Future Worth", variable=switch_variable2,
                            indicatoron=False, value=3, width=10,command=setValues)
G_button = Radiobutton(switch_frame, text="G", variable=switch_variable2,
                            indicatoron=False, value=4, width=10,command=setValues)
F_button.pack(side="left")
P_button.pack(side="left")
A_button.pack(side="left")
G_button.pack(side="left")

ent.pack()
Button(root,
    text="Calculate",command=evaluate).pack()
root.mainloop()
