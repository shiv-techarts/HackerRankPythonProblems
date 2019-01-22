# https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(string, sub_string):
    
    length = len(string)
    count = 0

    while length != 0:
        pos = string.find(sub_string)
        if pos != -1:
            count += 1
        
        string = string[pos + 2:]
        length = len(string)

    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
