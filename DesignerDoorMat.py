# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=false

def main():
    val = str(input())

    row = int(val.split()[0])
    col = int(val.split()[1])

    sep = ".|."
    dash = "-"

    for i in range(1, row, 2):
        print(str(sep * i).center(col, dash))

    print('WELCOME'.center(col, dash))

    for i in range(2, row, 2):
        print(str(sep * (row - i)).center(col, dash))


if __name__ == "__main__":
    main()
