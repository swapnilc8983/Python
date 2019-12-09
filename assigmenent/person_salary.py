def personSalary(salary, grade):
        hra = (20/100 * salary)
        da = (50/100 * salary)
        if grade == 'A' or 'a':
            allow = 1700
        elif grade == 'B' or 'b':
            allow = 1500
        else:
            allow = 1300
        
        pf = (11/100 * salary)          
        
        totalsalary = float( salary + hra + da + allow - pf)
        roundSalary = int(round(totalsalary))
        print("Total Salary: {}" .format(totalsalary)) 
        print("Round off Salary is: {}" .format(roundSalary))

salary = float(input("Basic Salary : "))
grade = str(input("Grade: "))

personSalary(salary, grade)


#------------Input------------
#Basic Salary : 10000.4
#Grade: a
#------------output------------
#Total Salary: 17600.636
#Round off Salary is: 17601
