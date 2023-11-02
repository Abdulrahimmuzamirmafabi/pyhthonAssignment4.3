from tuitions import Payment
from student import Student

#set_total_fees(cls, tuition, lib_fee, func_fee, med_fee):
Payment.set_total_fees(500, 50, 100, 150)

std1 = Student('Musa', 23, 500)
std2 = Student('Joe', 30, 650)
std3 = Student('Eve', 30, 1500)
#std4 = Student('Isa', 30, 1500)


stds = std1.get_all_students()

print(f'Total fees is {Payment.get_total_fees()}')

print('These are all the Students')
i=0
for std in stds:
    print(f'Student {i+1}\n')
    print(std,'\n')
    i+=1

print('These are students that have paid')
paid = Payment.get_paid_std()

for pa in paid:
    print(pa)