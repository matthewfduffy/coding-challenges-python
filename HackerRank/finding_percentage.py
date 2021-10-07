# Practice > Python > Basic Data Types > Finding the Percentage
"""
    The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

    Sample Input:
        3
        Krishna 67 68 69
        Arjun 70 98 63
        Malika 52 56 60
        Malika

    Sample Output:
        56.00


    Output Format:
    Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
"""
# base
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# user code
    total_marks = 0
    for i in range(3):
        total_marks += student_marks[query_name][i]
        i + 1
    student_avg = total_marks / 3
    
    
    def printC(answer):
        # x = str(answer)
        print("{:0.2f}".format(answer))
    
    printC(student_avg)

# Optimized
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))