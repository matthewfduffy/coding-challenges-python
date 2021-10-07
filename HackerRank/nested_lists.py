# Practice > Python > Basic Datatypes > Nested Lists
"""
    Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

    Example:        records = [["Chi", 20.0], ["Beta", 50.0], ["Alpha", 50.0]]
    Output:         alpha
                    beta
    
    Rationale:      The ordered list of scores is [20, 50]
                    There are two students with that score ("beta" and "alpha")

    Constraints:    2 <= N <= 5
                    There will always be one or more students having the second lowest grade.

    Input Format:   The first line contains an integer, N , the number of students.
                    The subsequent lines describe each student over lines.
                        - The first line contains a student's name.
                        - The second line contains their grade. 

    Output Format:  Print the name(s) of any student(s) having the second lowest grade in. 
                    If there are multiple students, order their names alphabetically and print each one on a new line.

    Sample Input:   5
                    Harry
                    37.21
                    Berry
                    37.21
                    Tina
                    37.2
                    Akriti
                    41
                    Harsh
                    39
    
    Sample Output:  Berry
                    Harry
"""
for _ in range(int(raw_input())):   # base
    scores = []
    name = raw_input()              # base
    score = float(raw_input())      # base
    scores.append(score)

sco