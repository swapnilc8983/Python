def personSalary(salary, grade):
        hra = (20/100 * salary)
        da = (50/100 * salary)
        if grade == 'A':
            allow = 1700
        elif grade == 'B':
            allow = 1500
        else:
            allow = 1300
        
        pf = (11/100 * salary)          
        
        totalsalary = round(float( salary + hra + da + allow - pf))
        print("Total Salary: {}" .format(totalsalary)) 

salary = float(input("Basic Salary : "))
grade = str(input("Grade: ").capitalize())

personSalary(salary, grade)

#------------
#Input: 
#Basic Salary : 10000
#Grade: a
#--------------
#output: 
#Total Salary: 17600
#------------
