import random
from tkinter import *
from tkinter import filedialog,messagebox

import randint
import datetime

operator = ''

food_price = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
drink_price = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
dessert_price = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def button_click(character):
    global operator
    operator = operator + character
    calculator_display.delete(0, END)
    calculator_display.insert(END, operator)

def delete_all():
    global operator
    operator = ''
    calculator_display.delete(0,END)

def get_result():
    global operator
    result = str(eval(operator))
    calculator_display.delete(0,END)
    calculator_display.insert(END,result)
    operator = ''
def review_check():
    x = 0
    for b in food_box:
        if food_variables[x].get() == 1:
            food_box[x].config(state=NORMAL)
            food_box[x].delete(END,0)
            if food_box[x].get() == '0':
                food_box[x].delete(0,END)
            food_box[x].focus()
        else:
            food_box[x].config(state=DISABLED)
            food_text[x].set('0')
        x += 1

    x = 0
    for b in drink_box:
        if drink_variables[x].get() == 1:
            drink_box[x].config(state=NORMAL)
            drink_box[x].delete(END,0)
            if drink_box[x].get() == '0':
                drink_box[x].delete(0, END)
            drink_box[x].focus()
        else:
            drink_box[x].config(state=DISABLED)
            drink_text[x].set('0')
        x += 1
    x = 0
    for b in dessert_box:
        if dessert_variables[x].get() == 1:
            dessert_box[x].config(state=NORMAL)
            dessert_box[x].delete(END,0)
            if dessert_box[x].get() == '0':
                dessert_box[x].delete(0, END)
            dessert_box[x].focus()
        else:
            dessert_box[x].config(state=DISABLED)
            dessert_text[x].set('0')
        x += 1

def total_calculation():
    food_subtotal = 0
    p=0
    for unit in food_text:
        food_subtotal = food_subtotal + (float(int(unit.get()) * food_price[p]))
        p += 1

    drink_subtotal = 0
    p=0
    for unit in drink_text:
        drink_subtotal = drink_subtotal + (float(int(unit.get()) * drink_price[p]))
        p += 1

    dessert_subtotal = 0
    p=0
    for unit in dessert_text:
        dessert_subtotal = dessert_subtotal + (float(int(unit.get()) * dessert_price[p]))
        p += 1

    my_subtotal = food_subtotal + drink_subtotal + dessert_subtotal
    my_tax = my_subtotal * 0.11
    my_total = my_subtotal + my_tax

    food_cost_var.set(f"Rs.{round(food_subtotal,2)}")
    drink_cost_var.set(f"Rs.{round(drink_subtotal, 2)}")
    dessert_cost_var.set(f"Rs.{round(dessert_subtotal, 2)}")
    subtotal_cost_var.set(f"Rs.{round(my_subtotal, 2)}")
    taxes_cost_var.set(f"Rs.{round(my_tax, 2)}")
    total_cost_var.set(f"Rs.{round(my_total, 2)}")

def invoice_display():
    invoice_text.delete(1.0,END)
    invoice_number = f'N# - {random.randint(1000,9999)}'
    my_date = datetime.datetime.now()
    invoice_date = f'{my_date.month}/{my_date.day}/{my_date.year} - {my_date.hour}:{my_date.minute}'
    invoice_text.insert(END, f'Information: \t{invoice_number}\t\t\t{invoice_date}\n')
    invoice_text.insert(END, f'*' * 76 + '\n')
    invoice_text.insert(END, f'Items \t\t Quantity\t ItemsCost\n')
    invoice_text.insert(END, f'-' * 91 + '\n')
    x=0
    for f in food_text:
        if f.get() != '0':
            invoice_text.insert(END, f'{food_list[x]}\t\t  {f.get()}\t'
                                     f'    {round(int(f.get()) * food_price[x],2)}\n')
        x += 1
    x=0
    for d in drink_text:
        if d.get() != '0':
            invoice_text.insert(END, f'{drink_list[x]}\t\t  {d.get()}\t'
                                     f'    {round(int(d.get()) * drink_price[x],2)}\n')
        x += 1
    x=0
    for e in dessert_text:
        if e.get() != '0':
            invoice_text.insert(END, f'{dessert_list[x]}\t\t  {e.get()}\t'
                                     f'    {round(int(e.get()) * dessert_price[x],2)}\n')
        x += 1

    invoice_text.insert(END,f'*' * 76 + '\n')
    invoice_text.insert(END,f'Food Subtotal: {food_cost_var.get()}\n')
    invoice_text.insert(END,f'Drink Subtotal: {drink_cost_var.get()}\n')
    invoice_text.insert(END,f'Food Subtotal: {dessert_cost_var.get()}\n')
    invoice_text.insert(END,f'*' * 76 + '\n')
    invoice_text.insert(END, f'Subtotal: {subtotal_cost_var.get()}\n')
    invoice_text.insert(END, f'Tax total: {taxes_cost_var.get()}\n')
    invoice_text.insert(END, f'Total: {total_cost_var.get()}\n')
    invoice_text.insert(END, f'*' * 76 + '\n')
    invoice_text.insert(END,f'See you soon.....')

def save_invoice():
    invoice_info = invoice_text.get(1.0,END)
    invoice_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    invoice_file.write(invoice_info)
    invoice_file.close()
    messagebox.showinfo('Notification','Your Invoice is saved')

def reset_menu():
    invoice_text.delete(0.1,END)
    for text in food_text:
        text.set('0')
    for text in drink_text:
        text.set('0')
    for text in dessert_text:
        text.set('0')

    for box in food_box:
        box.config(state=DISABLED)
    for box in drink_box:
        box.config(state=DISABLED)
    for box in dessert_box:
        box.config(state=DISABLED)

    for var in food_variables:
        var.set(0)
    for var in drink_variables:
        var.set(0)
    for var in dessert_variables:
        var.set(0)

    food_cost_var.set('')
    drink_cost_var.set('')
    dessert_cost_var.set('')
    subtotal_cost_var.set('')
    taxes_cost_var.set('')
    total_cost_var.set('')

#Initialize application
application = Tk()

#Change app title

application.title("My Resturant Invoice System")

#Change background color

application.config(bg='burlywood')

# Restric the maximum size & window size

application.geometry('1250x550+0+0')
application.resizable(False,False)

# Prepare a top panel
top_panel = Frame(application, bd=1, relief=FLAT)
top_panel.pack(side=TOP)

# Prepare tag

title_tag = Label(top_panel, text='Invoice System', fg='azure4',font=('Dosis', 50),bg='burlywood',width=27)
title_tag.grid(row=0,column=0)

# Left Panel
left_panel = Frame(application, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)

#Cost Panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=60)
cost_panel.pack(side=BOTTOM)

# Food Panel

food_panel = LabelFrame(left_panel, text='Food', fg='azure4',font=('Dosis', 19, 'bold'), bd=1, relief=FLAT)
food_panel.pack(side=LEFT)

# Drink Panel

drink_panel = LabelFrame(left_panel, text='Drink', fg='azure4',font=('Dosis', 19, 'bold'), bd=1, relief=FLAT)
drink_panel.pack(side=LEFT)

# Dessert Panel

dessert_panel = LabelFrame(left_panel, text='Dessert', fg='azure4',font=('Dosis', 19, 'bold'), bd=1, relief=FLAT)
dessert_panel.pack(side=LEFT)


# right Panel
right_panel = Frame(application, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)

# calculator Panel
calculator_panel = Frame(right_panel, bd=1, relief=FLAT)
calculator_panel.pack()

# invoice Panel
invoice_panel = Frame(right_panel, bd=1, relief=FLAT)
invoice_panel.pack()

# Button Panel
button_panel = Frame(right_panel, bd=1, relief=FLAT)
button_panel.pack()

# Product list
food_list = ['Chicken','Lamb','Salmon','Hake','Kebabs','Pizza','Shawarma','Burger']
drink_list = ['Lemonode', 'Soda','Juice','Cola','Wine1', 'Wine2','Beer1','Beer2']
dessert_list = ['Ice Cream','Fruit','Brownies','Pudding','Cheesecake', 'Cake1','Cake2','cup cake']


#Food list display

counter = 0
food_variables = []
food_box = []
food_text = []
for food in food_list:
    food_variables.append('')
    food_variables[counter] = IntVar()
    food = Checkbutton(food_panel, text=food.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=food_variables[counter], command=review_check)
    food.grid(row=counter,column=0,sticky=W)
    #Create input boxes
    food_box.append('')
    food_text.append('')
    food_text[counter] = StringVar()
    food_text[counter].set('0')
    food_box[counter] = Entry(food_panel, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED, textvariable=food_text[counter])
    food_box[counter].grid(row=counter,column=1)
    counter +=1

#Food list display

counter = 0
drink_variables = []
drink_box = []
drink_text = []
for drink in drink_list:
    drink_variables.append('')
    drink_variables[counter] = IntVar()
    drink = Checkbutton(drink_panel, text=drink.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=drink_variables[counter], command=review_check)
    drink.grid(row=counter,column=0,sticky=W)
    # Create input boxes
    drink_box.append('')
    drink_text.append('')
    drink_text[counter] = StringVar()
    drink_text[counter].set('0')
    drink_box[counter] = Entry(drink_panel, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,textvariable=drink_text[counter])
    drink_box[counter].grid(row=counter, column=1)
    counter += 1
#Food list display

counter = 0
dessert_variables = []
dessert_box = []
dessert_text = []

for dessert in dessert_list:
    dessert_variables.append('')
    dessert_variables[counter] = IntVar()
    dessert = Checkbutton(dessert_panel, text=dessert.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=dessert_variables[counter],command=review_check)
    dessert.grid(row=counter,column=0,sticky=W)
    # Create input boxes
    dessert_box.append('')
    dessert_text.append('')
    dessert_text[counter] = StringVar()
    dessert_text[counter].set('0')
    dessert_box[counter] = Entry(dessert_panel, font=('Dosis', 18, 'bold'), bd=1, width=6, state=DISABLED,textvariable=dessert_text[counter])
    dessert_box[counter].grid(row=counter, column=1)

    counter +=1


# Cost Labels and input fields
food_cost_var = StringVar()

food_cost_label = Label(cost_panel, text='Food Cost', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
food_cost_label.grid(row=0,column=0)
food_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=food_cost_var)
food_cost_text.grid(row=0,column=1,padx=60)
# Cost Labels and input fields
drink_cost_var = StringVar()

drink_cost_label = Label(cost_panel, text='Drink Cost', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
drink_cost_label.grid(row=1,column=0)
drink_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=drink_cost_var)
drink_cost_text.grid(row=1,column=1,padx=60)
# Cost Labels and input fields
dessert_cost_var = StringVar()

dessert_cost_label = Label(cost_panel, text='Dessert Cost', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
dessert_cost_label.grid(row=2,column=0)
dessert_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=dessert_cost_var)
dessert_cost_text.grid(row=2,column=1,padx=60)

# Cost Labels and input fields
subtotal_cost_var = StringVar()

subtotal_cost_label = Label(cost_panel, text='Subtotal Cost', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
subtotal_cost_label.grid(row=0,column=2)
subtotal_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=subtotal_cost_var)
subtotal_cost_text.grid(row=0,column=3,padx=60)

# Cost Labels and input fields
taxes_cost_var = StringVar()

taxes_cost_label = Label(cost_panel, text='Taxes Cost', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
taxes_cost_label.grid(row=1,column=2)
taxes_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=taxes_cost_var)
taxes_cost_text.grid(row=1,column=3,padx=60)

# Cost Labels and input fields
total_cost_var = StringVar()

total_cost_label = Label(cost_panel, text='Total Cost', font=('Dosis', 12, 'bold'), bg='azure4',fg='white')
total_cost_label.grid(row=2,column=2)
total_cost_text = Entry(cost_panel, font=('Dosis', 12, 'bold'), bd=1, width=10, state='readonly', textvariable=total_cost_var)
total_cost_text.grid(row=2,column=3,padx=60)

#Buttons
buttons = ['total','invoice','save','reset']
created_buttons = []
column = 0

for button in buttons:
    button = Button(button_panel, text=button.title(), font=('Dosis',14,'bold'), fg='white',bg='azure4',bd=1,width=9)
    created_buttons.append(button)
    button.grid(row=0,column=column,)
    column += 1
created_buttons[0].config(command= total_calculation)
created_buttons[1].config(command= invoice_display)
created_buttons[2].config(command= save_invoice)
created_buttons[3].config(command= reset_menu)

#Invoice area
invoice_text = Text(invoice_panel,font=('Dosis',12,'bold'),bd=1,width=51, height=10)
invoice_text.grid(row=0,column=0)

#Calculator

calculator_display = Entry(calculator_panel, font=('Dosis',16,'bold'), bd=1,width=38)
calculator_display.grid(row=0,column=0,columnspan=4)
calculator_buttons = ['7','8','9','+',
                      '4','5','6','-',
                      '1','2','3','x',
                      'CE','DELETE','0','/']

#Calculator Posistion

stored_buttons = []

my_column = 0
my_row = 1
for button in calculator_buttons:
    button = Button(calculator_panel,text=button.title(),font=('Dosis',16,'bold'),fg='white',bg='azure4',bd=1,width=8)
    stored_buttons.append(button)
    button.grid(row=my_row,column=my_column)

    if my_column == 3:
        my_row += 1
    my_column += 1

    if my_column == 4:
        my_column = 0
stored_buttons[0].config(command=lambda: button_click('7') )
stored_buttons[1].config(command=lambda: button_click('8') )
stored_buttons[2].config(command=lambda: button_click('9') )
stored_buttons[3].config(command=lambda: button_click('+') )
stored_buttons[4].config(command=lambda: button_click('4') )
stored_buttons[5].config(command=lambda: button_click('5') )
stored_buttons[6].config(command=lambda: button_click('6') )
stored_buttons[7].config(command=lambda: button_click('-') )
stored_buttons[8].config(command=lambda: button_click('1') )
stored_buttons[9].config(command=lambda: button_click('2') )
stored_buttons[10].config(command=lambda: button_click('3') )
stored_buttons[11].config(command=lambda: button_click('*') )
stored_buttons[12].config(command=get_result)
stored_buttons[13].config(command=delete_all)
stored_buttons[14].config(command=lambda: button_click('0') )
stored_buttons[15].config(command=lambda: button_click('/') )

#run the application as loop
application.mainloop()