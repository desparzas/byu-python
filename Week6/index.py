# Strip off any leading and trailing whitespace from each line.

# In addition to the name and the job title, also access the salary and the ID number and save them into variables. Display all four values in this format: name (ID: id_number), job_title - $salary. Don't forget to convert the salary to a number and display it with two decimals.

# The following shows the first few lines of expected output at this point.

with open('./data/hr_system.txt', 'r') as file:
    hr = file.read()
    people = hr.splitlines()
    for person in people:
        p = person.split()
        name = p[0]
        id = p[1]
        job_title = p[2]
        anual_salary = float(p[3])
        paycheck = anual_salary/24
        if job_title == 'Engineer':
            paycheck+=1000
        format_paycheck = '{:.2f}'.format(paycheck)
        print(name, ' (ID: ', id,'), ', job_title, ' - $', format_paycheck, sep='')
        