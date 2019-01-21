# https://www.hackerrank.com/challenges/word-order/problem

if __name__ == "__main__":
    n = int(input())

    word_dict = dict()

    for i in range(n + 1):
        try:
            key = str(input())
        except EOFError:
            break

        if key in word_dict.keys():
            count = word_dict[key]
            word_dict[key] = count + 1
        else:
            word_dict[key] = 1

    print(len(word_dict.keys()))
    print(' '.join([str(i) for i in word_dict.values()]))
