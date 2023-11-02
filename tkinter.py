from tkinter import *
from tkinter import ttk
import tkinter as tk

from tuitions import Payment
from student import Student

# Setting my window
window = Tk()
window.title("Fees Payments System")
window.config(padx=20, pady=20)
def add_fee():
     tuition = int(tuition_entry.get())
     lib_fee = int(lib_entry.get())
     func_fee = int(function_entry.get())
     med_fee = int(medical_entry.get())
     Payment.set_total_fees(tuition, lib_fee, func_fee, med_fee)
     total_fees_entry.delete(0)
     total_fees_entry.insert(0, string=f'Total fees is {Payment.get_total_fees()}')
stds = []
def student_details():
     global stds
     name = name_entry.get()
     age = age_entry.get()
     fees = int(fees_entry.get())
     std1 = Student(name, age, fees)
     stds = std1.get_all_students()
def print_students():
     output_text.insert(tk.END, 'These are all the Students')
     i=0
     for std in stds:
         output_text.insert(tk.END, f'\nStudent {i + 1}')
         output_text.insert(tk.END, f'\n{std}')
         i += 1
         output_text.insert(tk.END, '\nTHESE ARE STUDENTS THAT HAVE PAID')
         paid = Payment.get_paid_std()
     for pa in paid:
          output_text.insert(tk.END, f'\n{pa}')
          # Labels
setting_fees_label = ttk.Label(window, text='SETTING FEES', font=('bold'))
setting_fees_label.grid(row=0, column=1)
lib_label = ttk.Label(window, text='ENTER LIB FEE: ')
lib_label.grid(row=3, column=1)
tuition_label = ttk.Label(window, text='ENTER TUITION: ')
tuition_label.grid(row=2, column=1)
function_label = ttk.Label(window, text='ENTER FUNCTION FEE: ')
function_label.grid(row=4, column=1)
medical_label = ttk.Label(window, text='ENTER MEDICAL FEE: ')
medical_label.grid(row=5, column=1)
student_details_label = ttk.Label(window, text="ENTER THE STUDENTS DETAILS: ",
font=('bold'))
student_details_label.grid(row=8, column=2)
name_label = ttk.Label(window, text="ENTER STUDENT'S NAME: ")
name_label.grid(row=9, column=1)
age_label = ttk.Label(window, text="ENTER STUDENT'S AGE: ")
age_label.grid(row=10, column=1)
fees_label = ttk.Label(window, text='ENTER FEES PAID BY THE STUDENT: ')
fees_label.grid(row=11, column=1)
record_student_label = ttk.Label(window, text="DO YOU WANT TO RECORD THIS STUDENTS:")
record_student_label.grid(row=12, column=1)
no_more_student_label = ttk.Label(window, text="DON'T YOU WANT TO RECORD THIS STUDENTS:")
no_more_student_label.grid(row=13, column=1)

# Entries
tuition_entry = ttk.Entry(window)
tuition_entry.grid(row=2, column=2)
lib_entry = ttk.Entry(window)
lib_entry.grid(row=3, column=2)
function_entry = ttk.Entry(window)
function_entry.grid(row=4, column=2)
medical_entry = ttk.Entry(window)
medical_entry.grid(row=5, column=2)
total_fees_entry = ttk.Entry(window)
total_fees_entry.grid(row=7, column=1)
name_entry = ttk.Entry(window)
name_entry.grid(row=9, column=2)
age_entry = ttk.Entry(window)
age_entry.grid(row=10, column=2)
fees_entry = ttk.Entry(window)
fees_entry.grid(row=11, column=2)


# Buttons
total_fees_button = ttk.Button(window, text='Confirm fees', command=add_fee)
total_fees_button.grid(row=6, column=2)
record_student_button = ttk.Button(window, text='YES', command=student_details)
record_student_button.grid(row=12, column=2)
no_more_student_button = ttk.Button(window, text='NO', command=print_students)
no_more_student_button.grid(row=13, column=2)
print_button = ttk.Button(window, text='Print Students', command=print_students)
print_button.grid(row=14, column=2)
# outputs

output_text = Text(window)
output_text.grid(row=15, column=2)




window.mainloop()