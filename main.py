#Scroll to bottom to see solution
# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny', 'Jason', 'Quincy', 'Leah', 'Regina', 'Louis', 'Karina', 'Willy', 'Stephanie', 'Rita', 'Faith', 'Lisa', 'Kenneth', 'Jordan', 'Sade', 'Lindsay'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally','Stephanie', 'Rita', 'Faith', 'Lisa', 'Kenneth', 'Jordan', 'Sade', 'Lindsay']

#using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!

missing_students = school.difference(attendance_list)
print(missing_students)








































#Solution: Notice how we don't have to convert the attendance_list to a set...it does it for you.
#print(school.difference(attendance_list))


