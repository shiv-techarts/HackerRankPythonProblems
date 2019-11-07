#!/usr/bin/env python3

# Merge the Tools!
# https://www.hackerrank.com/challenges/merge-the-tools/problem


def merge_the_tools(string, k):
    data = []
    n = len(string)

    start = 0
    end = k

    while start < n:
        new_str = string[start:end]

        uniq = set()
        new_data = ''

        for ch in new_str:
            if not ch in uniq:
                uniq.add(ch)
                new_data += ch

        print(new_data)

        start += k
        end += k

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)