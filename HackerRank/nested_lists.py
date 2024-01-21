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
    
    Explanation:
    There are 5 students in this class whose names and grades are assembled to build the following list:

    python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

    The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.
"""
if __name__ == '__main__':
    name_list = []
    score_list = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        name_list.append(name)
        score_list.append(score)

    records = list(zip(name_list, score_list))
    records_sorted = sorted(records, key=lambda x: x[0])

    record_scores = [x[1] for x in records]
    sorted_record_scores = sorted(list(set(record_scores)))
    second_lowest = sorted_record_scores[1]

    for n,s in records_sorted:
        if s == second_lowest:
         print(n)