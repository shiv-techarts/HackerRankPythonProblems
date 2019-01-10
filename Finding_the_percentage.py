#
# https://www.hackerrank.com/challenges/finding-the-percentage/problem
#

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    total_marks = 0

    for marks in student_marks[query_name]:
        total_marks += marks

    print("{0:.2f}".format(total_marks/len(student_marks[query_name])))
