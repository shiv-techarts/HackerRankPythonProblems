# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

def print_rangoli(size):
    line = ""
    pattern_list = list()

    for i in range(size):
        line = line[:i] + chr((97 + (size - 1)) - i) + line[i - 1:]
        line_list = '-'.join([ val for val in line ])
        pattern_list.append(line_list)

    pattern = pattern_list[:]
    pattern_list.reverse()
    pattern.extend(pattern_list[1:])

    [ print(i.center(len(pattern[(size * 2 - 1) // 2]), "-")) for i in pattern ]

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
