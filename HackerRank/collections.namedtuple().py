"""
namedtuples are easy to create, lightweight object types.
They turn tuples into convenient containers for simple tasks.
With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

[Challenge]
Dr. John Wesley has a spreadsheet containing a list of student's IDs, grades, class, and name.
Your task is to help Dr. Wesley calculate the average grades of the students. 
(Average = Sum of all Grades / Total Students)

[Note]
1. Colums can be in any order. IDs, Grades, Class and Name can be written in any order in the spreadsheet.
2. Column names are ID, MARKS, CLASS and NAME. Spelling and case type won't change.

[Input]
The first line contains an integer N, the total number of students.
The second line contains the names of the columns in any order.
The next N lines contains the marks, IDs, Name and Class, under their respective column nammes.

[Output]
Print the average grade of each student to two decimal places.
"""
"""
[Sample Input]
5
ID  MARKS   NAME     CLASS
1   97      Raymond  7
2   50      Steven   4
3   91      Adrian   9
4   72      Stewart  5
5   80      Peter    6   

[Sample Output]
78.00
"""
from collections import namedtuple

class_size = int(input())
column_order = list(map(str, input().split()))
student = namedtuple('student', column_order)
grade = column_order.index('MARKS')
counter = 0

for _ in range(class_size):
    student_info = input().split()
    counter += int(student_info[grade])

counter = counter / class_size
print(format(counter, ".2F"))


# print(getattr(column_order, 'MARKS'))