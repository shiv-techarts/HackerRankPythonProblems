#
# https://www.hackerrank.com/challenges/nested-list/problem
#

def main():
        
    students = list()
    score_list = list()

    for _ in range(int(input())):
        name = input()
        score = float(input())

        students.append([name, score])
        score_list.append(score)

    score_list = list(set(score_list))
    score_list.sort()
    second_min = score_list[1]
    stu_second_min = list()

    for index in range(len(students)):
        if students[index][1] == second_min:
            stu_second_min.append(students[index][0])

    stu_second_min.sort()

    [print(name) for name in stu_second_min]


if __name__ == '__main__':
    main()

